// This function proxies a request to another Firebase function in a different project

const functions = require("firebase-functions");
const admin = require("firebase-admin"); // Needed if not already initialized
const { onCall, HttpsError } = require("firebase-functions/v2/https");
const { logger } = require("firebase-functions/v2");
const { GoogleAuth } = require('google-auth-library'); // For OIDC token generation
const fetch = (...args) => import('node-fetch').then(({ default: fetch }) => fetch(...args)); // Or use axios

// Initialize Firebase Admin SDK if not already done in your project
// Ensure this only runs once, e.g., by checking admin.apps.length
if (!admin.apps.length) {
  admin.initializeApp();
}

// Proxy function to securely call the token generation function in the other project
exports.proxyGetArcGISToken = onCall({
    region: "us-central1", // Match the region of your app/other functions if needed
    // Add memory/timeout options if necessary
    // memory: "256MiB",
    // timeoutSeconds: 60,
}, async (request) => { // 'request' contains { data, context }

    // Optional: Check if the user is authenticated (even anonymously) if needed
    // if (!request.auth) {
    //   logger.error("Proxy function called by unauthenticated user.");
    //   throw new HttpsError('unauthenticated', 'Authentication required.');
    // }
    // logger.info(`Proxy called by UID: ${request.auth?.uid || 'anonymous'}`);

    // *** REPLACE WITH THE ACTUAL URL of getArcGISTokenHttp in geolmapportal-prod ***
    const targetFunctionUrl = 'YOUR_GEOLMAPPORTAL_GETARCGISTOKENHTTP_FUNCTION_URL';

    if (!targetFunctionUrl || targetFunctionUrl === 'YOUR_GEOLMAPPORTAL_GETARCGISTOKENHTTP_FUNCTION_URL') {
        logger.error("Target function URL is not configured.");
        throw new HttpsError('internal', 'Proxy configuration error.');
    }

    logger.info(`Proxying request to: ${targetFunctionUrl}`);

    const auth = new GoogleAuth();

    try {
        // Get an OIDC token client for the target URL.
        // This will use the service account identity the proxy function runs as.
        logger.info("Generating OIDC token for target function...");
        const client = await auth.getIdTokenClient(targetFunctionUrl);
        logger.info("OIDC token client obtained.");

        // Make the authenticated request to the target function
        // client.request() automatically handles adding the Authorization: Bearer token header
        logger.info("Making authenticated request to target function...");
        const response = await client.request({
            url: targetFunctionUrl,
            method: 'POST', // Or 'GET' if your HTTP function accepts it
            // Add body/params if the target function expected any
            // body: JSON.stringify({ some: 'data' }),
            // headers: {'Content-Type': 'application/json'}
        });

        logger.info(`Received response from target function with status: ${response.status}`);

        // Check if the target function responded successfully
        if (response.status < 200 || response.status >= 300) {
             // Try to get error message from target function's response body
            let errorMessage = `Target function failed with status ${response.status}`;
            try {
                 // Assuming the target function sends plain text or JSON error details
                const errorBody = response.data; // google-auth-library client parses JSON by default
                errorMessage = typeof errorBody === 'string' ? errorBody : JSON.stringify(errorBody);
            } catch (e) { /* Ignore parsing error */ }

            logger.error("Target function returned error status.", {
                status: response.status,
                statusText: response.statusText,
                responseData: response.data // May contain error details from target
            });
            throw new HttpsError('internal', `Failed to retrieve token: ${errorMessage}`);
        }

        // Assuming the target function returns JSON: { token: "...", expires: ... }
        // client.request automatically parses JSON response into response.data
        const tokenData = response.data;

        if (!tokenData || !tokenData.token || !tokenData.expires) {
             logger.error("Received invalid or incomplete token data from target function", { responseData: tokenData });
             throw new HttpsError('internal', 'Received invalid token data from target service.');
        }

        logger.info("Successfully received ArcGIS token via proxy.");
        // Return the token data to the original client caller
        return {
            token: tokenData.token,
            expires: tokenData.expires
        };

    } catch (error) {
        logger.error('Error executing proxy function:', {
             errorMessage: error.message,
             errorDetails: error.response?.data, // Log potential response data from failed request
             stack: error.stack
         });

        // Throw a generic error back to the client
        // Check if it's already an HttpsError, otherwise wrap it
        if (error instanceof HttpsError) {
            throw error;
        } else {
            throw new HttpsError('internal', 'An error occurred while proxying the ArcGIS token request.');
        }
    }
});