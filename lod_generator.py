"""
UE5 LOD Tools
Utility functions for generating LODs on Static Meshes.

Functions:
    generate_lods(asset_path, lod_count) - Auto-generates LOD chain with default count of 4
"""

import unreal

def generate_lod(asset_path, lod_count = 4):

    # Load mesh
    mesh = unreal.EditorAssetLibrary.load_asset(asset_path)

    if not mesh:
        print(f"ERROR: Could not load asset at: {asset_path}")
        return False

    if not isinstance(mesh, unreal.StaticMesh):
        print(f"ERROR: Asset is not a StaticMesh {asset_path}")
        return False

    #Subsytem
    subsystem = unreal.get_editor_subsystem(unreal.StaticMeshEditorSubsystem)

    # Build Reduction Settings
    reduction_settings = []

    # Define the reduction triangle percentage for each LOD
    reduction_percentage = [1, 0.5, 0.25, 0.1]
    screen_sizes = [1, 0.3, 0.1, 0.05]

    for i in range(lod_count):
        lod_setting = unreal.StaticMeshReductionSettings(
            percent_triangles = reduction_percentage[i],
            screen_size = screen_sizes[i]
        )
        reduction_settings.append(lod_setting)

    # Disable LOD Screen Size AutoCompute
    reduction_option = unreal.StaticMeshReductionOptions(
        auto_compute_lod_screen_size = False,
        reduction_settings = reduction_settings
    )

    # Apply LOD
    result = subsystem.set_lods(mesh, reduction_option)

    # Save asset
    unreal.EditorAssetLibrary.save_asset(asset_path)

    print(f"SUCCESS: {mesh.get_name} - {result} LODs generated")
    return True


print(generate_lod("/Game/Meshes/SM_Box"))