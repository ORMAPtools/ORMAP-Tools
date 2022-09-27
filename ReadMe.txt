ORMAP Tools V3.0
9/10/2022

Toolbox and python script tools to support ORMAP functions. 
ArcPro 2.9.4 

Default.tbx contains these 4 tools. When tools reference an external python script, 
its name in in parentheses. 

  CreateDDAnnoFromLabels (AddDimAnno.py) - Creates dimension annotation from labels 
  UpdateMapIndex (UpdateMapIndex.py) - Updates mapindex attribues 
  UpdateORMAPArea (UpdateORMAPArea.py) - Updates required ORMAP attribute fields 
  ZoomToMap (no separate python script) 

To use the tools you could copy the Default.tbx file someplace convenient to you,
copy the Python scripts someplace convenient and  
then update the properties on each tool to reference the Python scripts.
For example, 

  1. Copy "Default.tbx" to your project folder. (Use File Explorer or use cut and paste in ArcGIS Pro's catalog.)
  3. Copy python scripts to your project folder. 
  4. For each tool in the toolbox that references a separate Python script, 
  -- open Properties/Execution, and 
  -- change the "Script File" path to reference the new location.


Customizations: 

There are hard-coded values in the Python files that you can change for your site.
Customizing scripts requires you to have a working knowledge of tools and python. 

Zoom To Map - This tool assumes you have layers called Taxlot and MapIndex.  
To change the layers you must open the properties/validation and change them.  
If you have other layers you wish to filter then change the properties/parameters 
and change the FilterLayers value list. 

UpdateMapIndex - This Tool assumes you have a layer called MapIndex. To change 
the layers you must open the properties/validation and change them and change 
the UpdateMapIndex.py python script. To change options for town,range,section,qtr, 
and others you must open the properties/parameters and change the value list for 
those you wish to change. 

CreateDDAnnoFromLabels - This tool assumes you have layers called Taxlot_lines 
and MapIndex.  If you have additional Taxlot_lines labels you wish to reference 
you must change the value list by opening the Properties/Parameters menu and 
change the LabelAnnoStyle Value list. If you have different layer names you must 
change the Properties/Validation and change layer names and also update 
the CreateDDAnnoFromLabels.py python script and change them as well. 



