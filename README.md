# ORMAP-Tools

ORMAP Tools V2.0
1/16/2022

Toolbox and python script tools to support ORMAP functions.
ArcPro (2.8.3)

## Tools

The toolbox file ORMAPToolsV2.tbx contains these tools:

    CreateDDAnnoFromLabels (Python Script: AddDimAnno.py) 
    UpdateMapIndex (Python Script: UpdateMapIndex.py) 
    Zoom To Map (Python: no separate file)

The code for the first two is in separate files.

There is not a separate file for Zoom To Map because the code is embedded in the
toolbox. Open Properties and click on the Validation item to see it.

## To Install

1. Add "ORMAPToolsV2.tbx" to your ArcPro project
2. (Optionally) copy the tools from "ORMAPToolsV2.tbx" to your tool box
3. Copy the python scripts (AddDimAnno.py and UpdateMapIndex.py) to your tool script location
4. For each tool that references a script,
   * Open Properties/General
   * Change Script File path to reference your location

## Customization

Customizing scripts requires you to have a working knowledge of tools and python.

**Zoom To Map** - This tool assumes you have layers called Taxlot and MapIndex.  To change the layers you must open the properties/validation and change them.  If you have other layers you wish to filter then change the properties/parameters and change the FilterLayers value list.

**UpdateMapIndex** - This Tool assumes you have a layer called MapIndex. To change the layers you must open the properties/validation and change them and change the UpdateMapIndex.py python script. To change options for town,range,section,qtr, and others you must open the properties/parameters and change the value list for those you wish to change.

**CreateDDAnnoFromLabels** - This tool assumes you have layers called Taxlot_lines and MapIndex.  If you have additional Taxlot_lines labels you wish to reference you must change the value list by opening the Properties/Parameters menu and change the LabelAnnoStyle Value list. If you have different layer names you must change the Properties/Validation and change layer names and also update the CreateDDAnnoFromLabels.py python script and change them as well.

