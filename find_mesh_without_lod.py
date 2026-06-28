"""
UE5 LOD Tools
Utility functions for finding mesh without LODs on Static Meshes.

Functions:
    find_meshes_without_lods(folder) - Scans folder for meshes missing LODs
"""

import unreal


def find_mesh_without_lods(folder = "/Game"):

    # Get the asset registry subsystem
    asset_registry = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = asset_registry.get_assets_by_path(folder, recursive = True)

    # Static Mesh Editor Subsystem
    subsystem = unreal.get_editor_subsystem(unreal.StaticMeshEditorSubsystem)

    missing_lod = []
    for asset in assets:
        asset_type = asset.asset_class_path.asset_name
        if asset_type != "StaticMesh":
            continue

        mesh = unreal.EditorAssetLibrary.load_asset(str(asset.package_name))

        if not mesh:
            continue

        lod_count = subsystem.get_lod_count(mesh)
        if lod_count <= 1:
            missing_lod.append({
                "name": str(asset.asset_name),
                "path": str(asset.package_name),
                "lod": lod_count
            })

    print(f"\n=== Meshes missing LODs ===")
    for item in missing_lod:
        print(f"Name: {item['name']} | LOD: {item['lod']} - LODs | Path: {item['path']}")
    print(f"\nTotal: {len(missing_lod)} meshes need LODs")

    return missing_lod

find_mesh_without_lods()
