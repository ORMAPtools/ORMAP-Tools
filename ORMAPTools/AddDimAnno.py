# AddDimAnno.py
#
# Creates dimension annotation from new TaxlotLine Labels using the ConvertLabelsToAnnotation tool.
#
# Tool is run from ArcPro ToolBox/Tool - "CreateDDAnnoFromLabels" in default.tbx
#
#
# Database Required - In local folder TownEd.gdb and Default.gdb 
# 
# Steps
# 1. Get parameter values
# 2. Set Map Layers and default paths
# 3. Set temporary layers (also make sure they are deleted
# 4. Make Anno from label and append to anno class 
# 5. select and update newly added anno
#
# Dean - Spring 2021 

import arcpy, os

# 1. Get parameter values 
AnnoStyle = arcpy.GetParameterAsText(0)
TaxlotLinesSelected = arcpy.GetParameterAsText(1)
MapIndexCount = arcpy.GetParameterAsText(2)
MapNumber = arcpy.GetParameterAsText(3)
MapScale = arcpy.GetParameterAsText(4)
LabelClass = arcpy.GetParameterAsText(5)
AnnoLayer = arcpy.GetParameterAsText(6)
TaxlotLinesLayer = arcpy.GetParameterAsText(7)
MapIndexLayer = arcpy.GetParameterAsText(8)

#2. Set Map Layers and default paths  

thisProject = arcpy.mp.ArcGISProject("CURRENT")
Map = thisProject.activeMap
MapIndexLyr = Map.listLayers(MapIndexLayer)[0]
TaxlotLineLyr = Map.listLayers(TaxlotLinesLayer)[0]
AnnoLyr = Map.listLayers(AnnoLayer)[0]
FolderPath = thisProject.homeFolder 

#ScriptPath = os.getcwd()

OutGDB =  FolderPath + "\\TownEd.gdb"
WorkGDB =  FolderPath + "\\Default.gdb"

arcpy.AddMessage (FolderPath)
arcpy.AddMessage (WorkGDB)

# 3. Set temporary layers (also make sure they are deleted 

AnnoF = "Anno" + str(MapScale)
GroupAnno = "GroupAnno"
AnnoFPth = WorkGDB + "\\Taxlot_lines" +  AnnoF 
AnnoFLyr =  "Taxlot_lines" + AnnoF 
annoID = 9 

arcpy.AddMessage ("AnnoF: " + AnnoF)
    
# delete Temp layers 

arcpy.Delete_management (GroupAnno)
arcpy.Delete_management (AnnoFLyr)
arcpy.Delete_management(AnnoFPth)

# 4. Make Anno from label and append to anno class 

arcpy.cartography.ConvertLabelsToAnnotation('Map', 1200, WorkGDB, AnnoF, 'default', 'ONLY_PLACED', 'NO_REQUIRE_ID', 'STANDARD', '', '', GroupAnno, 'SINGLE_LAYER', TaxlotLineLyr, '', '')

arcpy.CalculateField_management(AnnoFPth, "SymbolID",0, "PYTHON3")

arcpy.Append_management(AnnoFLyr, AnnoLyr, "NO_TEST")

arcpy.AddMessage ("TempMade: " + AnnoFLyr)

# 5. select and update newly added anno 

arcpy.SelectLayerByAttribute_management(AnnoLyr, "NEW_SELECTION", "SymbolID = 0")

arcpy.CalculateField_management(AnnoLyr, "SymbolID",annoID, "PYTHON3")
arcpy.CalculateField_management(AnnoLyr, "AnnotationClassID",annoID, "PYTHON3")
arcpy.CalculateField_management(AnnoLyr, "MapNumber","'" + MapNumber + "'", "PYTHON3")

# Turn Off Labels

for lblClass in TaxlotLineLyr.listLabelClasses():
    lblClass.visible = False
    
# Cleanup temp layers 

arcpy.Delete_management (GroupAnno)
arcpy.Delete_management (AnnoFLyr)
arcpy.Delete_management(AnnoFPth)










        

