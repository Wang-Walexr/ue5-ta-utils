"""
UE5 Tools
Utility functions for checking oversized texture assets.

Functions:
    find_oversized_textures() - Scan folder for oversized textures
"""

import unreal

def find_oversized_textures(folder = "/Game", max_size = 2048):
    """
    Scans a folder for textures exceeding the maximum recommended size.

    Args:
        folder (str): Content Browser path to scan. Default /Game/
        max_size (int): Maximum recommended texture dimension in pixels. Default 2048 (2K).

    Returns:
        list: List of dicts with texture info for flagged assets.

    Example:
        find_oversized_textures("/Game/Textures/", max_size=1024)
    """

    # Get the asset registry subsystem
    asset_registry = unreal.AssetRegistryHelpers.get_asset_registry()
    assets = asset_registry.get_assets_by_path(folder, recursive = True)

    oversized_textures = []

    for asset in assets:
        asset_type = asset.asset_class_path.asset_name

        if asset_type != "Texture2D":
            continue

        texture = unreal.EditorAssetLibrary.load_asset(asset.package_name)

        if not texture:
            continue

        texture_width = texture.blueprint_get_size_x()
        texture_height = texture.blueprint_get_size_y()

        if texture_width > max_size or texture_height > max_size:
            oversized_textures.append({
                "Name": str(asset.asset_name),
                "Path": str(asset.package_name),
                "Width": texture_width,
                "Height": texture_height,
                "Recommended": max_size
        })

    print(f"\n=== Oversized Textures (max {max_size}px) ===")
    for item in sorted(oversized_textures, key=lambda x: x['Width'], reverse=True):
        print(f" Name: {item['Name']} | Width: {item['Width']} x Height: {item['Height']} | Path: {item['Path']}")
    print(f"\nTotal: {len(oversized_textures)} textures exceed {max_size}px")

    return oversized_textures


find_oversized_textures(folder = "/Game", max_size = 2048)