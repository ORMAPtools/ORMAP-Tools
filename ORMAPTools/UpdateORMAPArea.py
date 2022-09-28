# Update Legal Acres
#
#
# Called from UpdateORMAPAreaTool
#
# Uses current project file and layer for Taxlot
# 
# For selected taxlots it updates the legal acres needed for ORMAP
# Dean - Spring 2022
#
import sys
import arcpy 

Taxlot = "Taxlot"

# 2. Set Layer and ensure only 1 feature selected ---------------------------

thisProject = arcpy.mp.ArcGISProject("CURRENT")      
editMap = thisProject.activeMap 
MapLayer = editMap.listLayers(Taxlot)[1]

MapLayerCnt = int(arcpy.GetCount_management(MapLayer).getOutput(0))
arcpy.AddMessage (MapLayerCnt)

# Check if you have one map feature selected - if not quit - also check for mapnumber issues (ie. quarter without section) --------------

if MapLayerCnt == 0 or MapLayerCnt > 200:
    arcpy.AddError ("Must not have correct number of taxlots selected ")
    sys.exit(0)

arcpy.CalculateField_management(MapLayer, "TaxlotFeet","!CalculatedArea!", "PYTHON3")
arcpy.AddMessage ("TaxlotFeetDone")
arcpy.CalculateField_management(MapLayer, "TaxlotAcre","!CalculatedArea! / 43560", "PYTHON3")
arcpy.AddMessage ("TaxlotAcreDone" )
arcpy.CalculateField_management(MapLayer, "MapAcres","!Shape_Area! / 43560", "PYTHON3")
arcpy.AddMessage ("MapAcres Done")
arcpy.AddMessage ('Calcs are done')               







