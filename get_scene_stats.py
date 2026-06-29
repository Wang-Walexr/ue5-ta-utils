"""
UE5 Tools
Utility functions for getting the statistics of objects in the scene.

Functions:
    get_scene_stats() - Scan the level to get scene statistics
"""

import unreal

def get_scene_stats():
    """
    Scans the level to get basic scene statistics useful for optimization auditing.

    Returns:
        dict: Scene statistics including actor counts by type.

    Example:
        stats = get_scene_stats()
    """

    # Get level actors
    scene_editor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    all_actors = scene_editor_subsystem.get_all_level_actors()


    # Asset Type Map
    ASSET_TYPE_MAP = {
        "StaticMesh": 0,
        "SkeletalMesh": 0,
        "Light": 0,
        "ExponentialHeightFog": 0,
        "SkyAtmosphere": 0,
        "VolumetricCloud": 0,
        "Niagara": 0,
        "BP": 0,
    }


    for actor in all_actors:
        actor_type = actor.get_class().get_name()

        for key in ASSET_TYPE_MAP.keys():
            if key in actor_type:
                ASSET_TYPE_MAP[key] += 1


    stats = ASSET_TYPE_MAP
    stats.update({"TotalActors": len(all_actors)})

    print(f"\n=== Scene Statistics ===")
    for item in stats:
        print(f"  {item}:       {stats[item]}")



    if stats["Light"] > 10:
        print(f"\n  WARNING: {stats['Light']} lights in scene. Consider baking static lights to reduce draw call cost.")


    if stats["StaticMesh"] > 30:
        print(f"\n  WARNING: {stats['StaticMesh']} static mesh actors. Check for instancing opportunities.")

    return stats

get_scene_stats()