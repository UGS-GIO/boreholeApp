import arcpy
#script must be run in Python 2.7

#Define tables to update - using complete sde connection string
unit=r"C:\Users\marthajensen\AppData\Roaming\ESRI\Desktop10.7\ArcCatalog\sde@ugshazards.sde\ugshazards.sde.borehole_unit_table"
sample=r"C:\Users\marthajensen\AppData\Roaming\ESRI\Desktop10.7\ArcCatalog\sde@ugshazards.sde\ugshazards.sde.borehole_sample_table"
borehole=r"C:\Users\marthajensen\AppData\Roaming\ESRI\Desktop10.7\ArcCatalog\sde@ugshazards.sde\ugshazards.sde.borehole_locations"

####################Count existing records ########################################
count=arcpy.GetCount_management(in_rows=borehole)

print ("The count of existing borehole locations is " + str(count))

count1=arcpy.GetCount_management(in_rows=sample)
print("The count of existing samples is " + str(count1))

count2=arcpy.GetCount_management(in_row=unit)
print("The count of existing units is " + str(count2))

###############################################Truncate#########################################

#Truncate existing tables
arcpy.TruncateTable_management(in_table=unit)
arcpy.TruncateTable_management(in_table=sample)
arcpy.TruncateTable_management(in_table=borehole)
print ("Finished truncating all data, starting to append new records")

#################################################Append##########################################

#Append data to existing tables - using tables Gordon created (change inputs here if needed-highly likely you will need to change the gdb name because they are usually not overwritten) Control - shift - r for find and replace in the field_mapping (field_mapping must contain entire path)
#inputs - need to redefine each time. Whole location string must exist in append for it to run

newborehole="'G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Borehole_Locations'"
newsample="'G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Sample_Table'"
newunit="'G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Unit_Table'"

arcpy.Append_management(inputs=newborehole, target=borehole, schema_type="NO_TEST", field_mapping='boreid "BoreID" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Borehole_Locations,boreid,-1,-1;ugs_gdid "UGS_GDID" true true false 4 Long 0 10 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Borehole_Locations,ugs_gdid,-1,-1;consultant "Consultant" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Borehole_Locations,consultant,-1,-1;projectid "ProjectID" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Borehole_Locations,projectid,-1,-1;udot_pin "UDOT_PIN" true true false 4 Long 0 10 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Borehole_Locations,udot_pin,-1,-1;project_name "Project_Name" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Borehole_Locations,project_name,-1,-1;latitude "Latitude" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Borehole_Locations,latitude,-1,-1;longitude "Longitude" true true false 8 Double 8 38 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Borehole_Locations,longitude,-1,-1;coordinate_source "Coordinate_Source" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Borehole_Locations,coordinate_source,-1,-1;elevation_ft "Elevation_Ft" true true false 8 Double 8 38 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Borehole_Locations,elevation_ft,-1,-1;elevation_source "Elevation_Source" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Borehole_Locations,elevation_source,-1,-1;date_completed "Date_Completed" true true false 8 Date 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Borehole_Locations,date_completed,-1,-1;geologic_unit "Geologic_Unit" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Borehole_Locations,geologic_unit,-1,-1;exploration_type "Exploration_Type" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Borehole_Locations,exploration_type,-1,-1;exploration_method "Exploration_Method" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Borehole_Locations,exploration_method,-1,-1;exploration_equiptment "Exploration_Equiptment" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Borehole_Locations,exploration_equipment,-1,-1;gw_depth "GW_Depth" true true false 8 Double 8 38 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Borehole_Locations,gw_depth,-1,-1;hammer_type "Hammer_Type" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Borehole_Locations,hammer_type,-1,-1;correctedn1_60 "CorrectedN1_60" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Borehole_Locations,correctn1_60,-1,-1;completion "Completion" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Borehole_Locations,completion,-1,-1;bedrock_refusal "Bedrock_Refusal" true true false 4 Long 0 10 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Borehole_Locations,bedrock_refusal,-1,-1;enteredby "EnteredBy" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Borehole_Locations,enteredby,-1,-1;notes "Notes" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Borehole_Locations,notes,-1,-1;report_url "report_url" true true false 100 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Borehole_Locations,report_url,-1,-1;globalid "globalid" false false false 38 GlobalID 0 0 ,First,#;databasedate "databasedate" true true false 8 Date 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Borehole_Locations,databasedate,-1,-1', subtype="")
arcpy.Append_management(inputs=newsample, target=sample, schema_type="NO_TEST", field_mapping='boreid "BoreID" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Sample_Table,boreid,-1,-1;samplenumber "SampleNumber" true true false 4 Long 0 10 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Sample_Table,samplenumber,-1,-1;sampleupperdepth "SampleUpperDepth" true true false 8 Double 8 38 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Sample_Table,sampleupperdepth,-1,-1;samplelower_depth "SampleLower Depth" true true false 8 Double 8 38 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Sample_Table,samplelower_depth,-1,-1;samplemethod "SampleMethod" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Sample_Table,samplemethod,-1,-1;nvalue "Nvalue" true true false 4 Long 0 10 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Sample_Table,nvalue,-1,-1;classification "Classification" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Sample_Table,classification,-1,-1;gravel_percent "Gravel_Percent" true true false 4 Long 0 10 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Sample_Table,gravel_percent,-1,-1;sand_percent "Sand_Percent" true true false 4 Long 0 10 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Sample_Table,sand_percent,-1,-1;fines_percent "Fines_Percent" true true false 4 Long 0 10 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Sample_Table,fines_percent,-1,-1;labmoisture_percent "LabMoisture_Percent" true true false 8 Double 8 38 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Sample_Table,labmoisture_percent,-1,-1;labdrydensity_pcf "LabDryDensity_pcf" true true false 8 Double 8 38 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Sample_Table,labdrydensity_pcf,-1,-1;ll "LL" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Sample_Table,ll,-1,-1;pl "PL" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Sample_Table,pl,-1,-1;pi "PI" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Sample_Table,pi,-1,-1;sct_percent "SCT_Percent" true true false 8 Double 8 38 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Sample_Table,sct_percent,-1,-1;sct_dry_percent "SCT_Dry_Percent" true true false 8 Double 8 38 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Sample_Table,sct_dry_percent,-1,-1;shear_type "Shear_Type" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Sample_Table,shear_type,-1,-1;shearangle_degree "ShearAngle_Degree" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Sample_Table,shearangle_degree,-1,-1;shearcohesion_psi "ShearCohesion_PSI" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Sample_Table,shearcohesion_psi,-1,-1;resistivity_ohm_cm "Resistivity_ohm_cm" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Sample_Table,resistivity_ohm_cm,-1,-1;sulfates_ppm "Sulfates_ppm" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Sample_Table,sulfates_ppm,-1,-1;chlorides_ppm "Chlorides_ppm" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Sample_Table,chlorides_ppm,-1,-1;organics_percent_weight "Organics_Percent_Weight" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Sample_Table,organics_percent_weight,-1,-1;ph "pH" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Sample_Table,ph,-1,-1;notes "Notes" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Sample_Table,notes,-1,-1', subtype="")
arcpy.Append_management(inputs=newunit, target=unit, schema_type="NO_TEST", field_mapping='boreid "BoreID" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Unit_Table,boreid,-1,-1;upperdepth "UpperDepth" true true false 8 Double 8 38 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Unit_Table,upperdepth,-1,-1;lowerdepth "LowerDepth" true true false 8 Double 8 38 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Unit_Table,lowerdepth,-1,-1;uscs "USCS" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Unit_Table,uscs,-1,-1;unitname "UnitName" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Unit_Table,unitname,-1,-1;fieldmoisture "FieldMoisture" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Unit_Table,fieldmoisture,-1,-1;fieldcolor "FieldColor" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Unit_Table,fieldcolor,-1,-1;fielddensity "FieldDensity" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Unit_Table,fielddensity,-1,-1;fieldconsistency "FieldConsistency" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Unit_Table,fieldconsistency,-1,-1;notes "Notes" true true false 8000 Text 0 0 ,First,#,G:/Shared drives/UGS_Hazards_Geotech/Geotechnical Database/Borehole_Data_WGS84_20210225.gdb/Unit_Table,notes,-1,-1', subtype="")

print ("Finished appending new records")

####################Count new records########################################

# Get count of points in feature class
count3=arcpy.GetCount_management(in_rows=borehole)

print ("The count of borehole locations is now " + str(count3))

count4=arcpy.GetCount_management(in_rows=sample)
print("The count of samples is now " + str(count4))

count5=arcpy.GetCount_management(in_row=unit)
print("The count of units is now " + str(count5))