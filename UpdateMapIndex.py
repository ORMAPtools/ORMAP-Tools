# Update MapIndex
# This python goes with the UpdateMapIndex Script in the template
#
# In the tool you can enter all the basic map info and it will update it.
#
# You can also adjust many of the parameters to cutomize the tool so that fields like town and range
# will have a pull down list for only those in your township. If you mapindex layer is not Mapindex you
# will need to change the layer name in the tool validation parameters (MapIndexLayer = GetParameterAsText(22)
#
# Tool is run from ArcPro ToolBox/Tool - "UpdateMapIndexReset" in default.tbx 
#
# Steps
# 1. Get Values from paramters. 
# 2. Get Mapindex layer and ensure only one feature is selected and basic mapnumber parameters are set
# 3. Calc Map Title - Any customization of the map title will go here
# 4. Use update cursor to update selected mapindex feature including ormap numbers 
# 
#
# Dean - 1/25/2020
#
# Update: updated to be sure to really exit if more then one map selected - Dean March 2021

import sys
import arcpy 

# 1. Get values from parameters  ----

MapNumber = str(arcpy.GetParameterAsText(0))
MapScale = arcpy.GetParameterAsText(1)
County = str(arcpy.GetParameterAsText(2))
ReliaCode = arcpy.GetParameterAsText(3)
Town = str(arcpy.GetParameterAsText(4))
TownPart = str(arcpy.GetParameterAsText(5))
TownDir = str(arcpy.GetParameterAsText(6))
Range = str(arcpy.GetParameterAsText(7))
RangePart = str(arcpy.GetParameterAsText(8))
RangeDir = str(arcpy.GetParameterAsText(9))
Section = str(arcpy.GetParameterAsText(10))
QuarterSection = str(arcpy.GetParameterAsText(11))
QtrQtrSection = str(arcpy.GetParameterAsText(12))
Anomaly = str(arcpy.GetParameterAsText(13))
MapSuffixType = str(arcpy.GetParameterAsText(14))
MapSuffixNumber = str(arcpy.GetParameterAsText(15))
CityName = str(arcpy.GetParameterAsText(16))
PageName = str(arcpy.GetParameterAsText(17))
Book = arcpy.GetParameterAsText(18)
GroupName = str(arcpy.GetParameterAsText(19))
SecondTitle = str(arcpy.GetParameterAsText(20))
MapAngle = arcpy.GetParameterAsText(21)
MapIndexLayer = str(arcpy.GetParameterAsText(22))

arcpy.AddMessage("MapIndex: " + MapIndexLayer)


# 2. Set Layer and ensure only 1 feature selected ---------------------------

thisProject = arcpy.mp.ArcGISProject("CURRENT")      
editMap = thisProject.activeMap 
MapLayer = editMap.listLayers(MapIndexLayer)[0]

MapLayerCnt = int(arcpy.GetCount_management(MapLayer).getOutput(0))
arcpy.AddMessage (MapLayerCnt)

# Check if you have one map feature selected - if not quit - also check for mapnumber issues (ie. quarter without section) --------------

if MapLayerCnt > 1:
    arcpy.AddError ("More then one feature selected")
    sys.exit(0) 
if QuarterSection == "0" and QtrQtrSection != "0":
    arcpy.AddError ("Quarter/Quarter is filled but Quarter is not")
    sys.exit(0)
if QuarterSection != "0" and Section == "00":
    arcpy.AddError ("Cannot have a section 00 with quartersections filled")
    sys.exit(0)
    
# 3. Calc Map Title----------------------Any county specific code for suffixes etc goes here ----------------------------------------
# T/R/S does a str/int to get rid of leading zeroes
 
QuarterTitles = ['',' N.E.1/4 ',' N.W.1/4 ',' S.W.1/4 ',' S.E.1/4 ']
Quarters = ['0','A','B','C','D']
Title = "T." + str(int(Town)) + " " + TownDir + ". R." + str(int(Range)) + " " + RangeDir + ". W.M."
if Section != "00":   
    QuarterTitle = ""
    QtrQtrTitle = "" 
    x = 0
    for q in Quarters:
        arcpy.AddMessage(x) 
        if q == QuarterSection:
            QuarterTitle = QuarterTitles[x]
        if q == QtrQtrSection:
            QtrQtrTitle = QuarterTitles[x] 
        x = x + 1
    Title = QtrQtrTitle + QuarterTitle + "SEC. " + str(int(Section)) + ' ' + Title

# 4. Calc Values with UpdateCursor ----------------------------------------------------------------
#                                         0           1          2       3          4            5       6        7           8           9           10          11 
with arcpy.da.UpdateCursor(MapLayer,['MapNumber','MapScale','County','ORMapNum','CityName','PageName','Book','GroupName','SecondTitle','ReliaCode','MapAngle',"MapTitle"]) as cursor:
    for row in cursor:
        row[0] = MapNumber
        #if row[1] is None:       
        row[1] = MapScale
        #if row[2] is None:               
        row[2] = County
        row[3] = County + Town + TownPart + TownDir + Range + RangePart + RangeDir + Section + QuarterSection + QtrQtrSection + Anomaly + MapSuffixType + MapSuffixNumber
        row[4] = CityName
        row[5] = PageName
        if Book.isnumeric(): row[6] = Book
        row[7] = GroupName
        row[8] = SecondTitle
        if ReliaCode.isnumeric(): row[9] = ReliaCode
        if MapAngle.isnumeric(): row[10] = MapAngle
        row[11] = Title 
        cursor.updateRow(row)
del row                







