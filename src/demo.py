import json
from analysis import (
    total_active_area,
    parcels_above_threshold,
    count_by_zone,
    intersecting_parcels,
)
from spatial import Parcel


def main():
    fp_parcels = "data/parcels_shapely_ready.json"

    # Load parcel data
    try:
        with open(fp_parcels, "r", encoding="utf-8") as file:
            parcels_data = json.load(file)
    except FileNotFoundError:
        print(f"File not found: {fp_parcels}")
        return
    except json.JSONDecodeError:
        print("Invalid JSON file.")
        return

    if not parcels_data:
        print("No parcels found.")
        return

    parcels = [Parcel.from_dict(p) for p in parcels_data]

    # Configuration
    threshold_area = 300  # sq.m.
    zone = "Residential"

    # What is the total area of all active parcels?
    print("Total active area:", total_active_area(parcels))

    # Which parcels exceed a threshold area? 
    large_parcels = parcels_above_threshold(parcels, threshold_area)
    print("First parcel above threshold:", large_parcels[0] if large_parcels else "None")

    # How many parcels per zone?
    print("Parcels per zone:", count_by_zone(parcels))

    # Which parcels intersect a proposed development boundary? 
    intersecting = intersecting_parcels(parcels, zone)
    print("First intersecting parcel:", intersecting[0] if intersecting else "None")


if __name__ == "__main__":
    main()