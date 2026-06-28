"""
UE5 Tools
Utility functions for checking bad naming conventions on assets.

Functions:
    check_names(folder = "/Game") - Scan folder for bad naming conventions
    print_result(passed_mesh, failed_mesh) - Print out the results in a readable format
"""

import unreal

NAMING_CONVENTION_MAP = {
    "StaticMesh": "SM_",
    "SkeletalMesh": "SKM_",
    "Material": "M_",
    "MaterialInstanceConstant": "MI_",
    "Texture2D": "T_",
    "Blueprint": "BP_",
}

def check_names(folder = "/Game"):
    """Check the naming convention in a given folder"""
    asset_registry = unreal.AssetRegistryHelpers.get_asset_registry() # Get the asset registry subsystem
    assets = asset_registry.get_assets_by_path(folder, recursive = True) # Get assets in the paths

    passed_mesh = []
    failed_mesh = []

    for asset in assets:
        asset_name = str(asset.asset_name)
        asset_type = str(asset.asset_class_path.asset_name)

        if asset_type not in NAMING_CONVENTION_MAP:
            continue

        expected_prefix = NAMING_CONVENTION_MAP[asset_type]

        if asset_name.startswith(expected_prefix):
            passed_mesh.append((asset_name, asset_type, str(asset.package_path)))
        else:
            failed_mesh.append((asset_name, asset_type, expected_prefix, str(asset.package_path)))

    return passed_mesh, failed_mesh

def print_result(passed_mesh, failed_mesh):
    """Print the results of the naming convention checks"""

    print("\n=== NAMING CONVENTION REPORT ===")
    print(f"\n + Passed {len(passed_mesh)}:")

    for asset_name, asset_type, path in passed_mesh:
        print(f" + {asset_name} | {asset_type} | {path}")

    print(f"\n - Failed {len(failed_mesh)}:")

    for asset_name, asset_type, expected_prefix, path in failed_mesh:
        print(f"\n - {asset_name} | {expected_prefix} | {asset_type} | {path}")

    print(f"\nTotal: {len(passed_mesh)} passed, {len(failed_mesh)} failed")

passed, failed = check_names("/Game")
print_result(passed, failed)


