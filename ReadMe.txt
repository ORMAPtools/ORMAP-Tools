ORMAP Tools V2.01 
3/18/2022 

Toolbox and python script tools to support ORMAP functions. 
ArcPr (2.8.3) 

Update 

ZoomTool Fix - When using SDE has a problem with null taxlots (fix sent from John) 

Tools 
Zoom To Map (Python Script: None) 
UpdateMapIndex (Python Script: UpdateMapIndex.py) 
CreateDDAnnoFromLabels (Python Script: AddDimAnno.py) 

To Install: 

1. Add "ORMAPToolsV2.tbx" to your ArcPro project 
2. Copy Tools from "ORMAPToolsV2.tbx"  to your tool box 
3. Copy python scripts to your tool script location 
4. For tools that reference Scripts 
-- Open Properties/General 
-- Change Script File path to reference the new location 

Customization: 

Customizing scripts requires you to have a working knolege of tools and python. 

Zoom To Map - This tool assumes you have layers called Taxlot and MapIndex.  To change the layers you must open the properties/validation and change them.  If you have other layers you wish to filter then change the properties/parameters and change the FilterLayers value list. 

UpdateMapIndex - This Tool assumes you have a layer called MapIndex. To change the layers you must open the properties/validation and change them and change the UpdateMapIndex.py python script. To change options for town,range,section,qtr, and others you must open the properties/parameters and change the value list for those you wish to change. 

CreateDDAnnoFromLabels - This tool assumes you have layers called Taxlot_lines and MapIndex.  If you have additional Taxlot_lines labels you wish to reference you must change the value list by opening the Properties/Parameters menu and change the LabelAnnoStyle Value list. If you have different layer names you must change the Properties/Validation and change layer names and also update the CreateDDAnnoFromLabels.py python script and change them as well. 



