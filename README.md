# UE5 Technical Artist Utilities

A growing collection of Python utility functions for Unreal Engine 5.7 Technical Artist workflows.

All functions use the UE5.7 subsystem pattern. No deprecated EditorScriptingUtilities calls.

## Modules

### lod_tools
LOD generation and auditing for Static Meshes.
- lod_generator.py : auto-generates a 4-LOD chain
- find_mesh_without_lod.py : scans for missing LODs


### naming_tools
Naming convention validation.
- name_checker.py : scans folder for convention violations
- (EUW version available in separate repo)

### texture_audit tool
Audit textures
- find_oversized_textures.py : Scan folder for oversized textures

## Usage

Run any script via UE5's Python console:
```python
exec(open(r"E:\path\to\lod_tools.py").read())
generate_lods("/Game/Meshes/SM_Rock")
```

## UE5 Version

Tested on UE5.7. Uses StaticMeshEditorSubsystem and AssetRegistryHelpers throughout.