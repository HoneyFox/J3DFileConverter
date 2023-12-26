A python tool to convert J3D model files for game Jane's Fleet Command.

NOTES:
  * Two python script files inside Blender3AddonScripts folder are to provide additional option for wavefront obj exporter in Blender 3.x.
  * The option "Rename objects with hierarchy info" will inject hierarchy info and its local offset into the object names.
  * You probably need to modify game folder path in AddToFCDB.bat.
  * The J3DFile.h contains pseudo code of file format. (but I didn't use C++ to write the tool since the language is a bit too heavy compared to python)
  * Not sure if Dangerous Waters also uses the same J3D format or not, I haven't tested it with DW.

Usage:
  * Copy two scripts in Blender3AddonScripts\io_scene_obj\ folder to corresponding folder under Blender3's \scripts\addons\io_scene_obj\ folder.
  * Use Blender to create your model.
  * Export the model to .obj file.
  * Drag the .obj file to ConvertOBJ.bat, a .J3D file will be generated at the same location of the .obj file.
  * Drag the .J3D file and all .BMP texture files used to AddToFCDB.bat. (.BMP should be 8bit for Jane's Fleet Command)

Remarks/Known Issues:
  * There are still some unknown fields in J3D format. Luckily they seem to be constant in most (if not all) J3D files.
  * Hierarchy doesn't support rotation/scaling, only offset/translation is supported. And even offset/translation is not actually tested yet.
  
