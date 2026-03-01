from pathlib import Path
import json
import analysis as a
from spatial import Parcel


def load_parcels(filepath: Path) -> list[Parcel]:
    """Load parcel data from JSON and convert to Parcel objects."""
    if not filepath.exists():
        raise FileNotFoundError(f"Parcel file not found: {filepath}")

    with filepath.open("r", encoding="utf-8") as file:
        parcels_data = json.load(file)

    if not parcels_data:
        raise ValueError("Parcel list is empty.")

    return [Parcel.from_dict(parcel) for parcel in parcels_data]


def save_summary(filepath: Path, summary: dict) -> None:
    """Save analysis summary to JSON."""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with filepath.open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)


def main():
    # File paths
    fp_parcels = Path("data/parcels_shapely_ready.json")
    fp_output = Path("output/summary.json")

    # Configuration
    threshold_area = 300  # square meters
    target_zone = "Residential"

    # Load data
    parcels = load_parcels(fp_parcels)

    # Run analysis
    total_active_area = a.total_active_area(parcels)
    large_parcels = a.parcels_above_threshold(parcels, threshold_area)
    count_per_zone = a.count_by_zone(parcels)
    intersecting = a.intersecting_parcels(parcels, target_zone)

    # Prepare summary
    summary = {
        "total_active_area": total_active_area,
        "parcels_above_threshold": large_parcels,
        "count_by_zone": count_per_zone,
        "intersecting_parcels": intersecting,
    }

    # Output
    print("\nAnalysis Results")
    print("----------------")
    for key, value in summary.items():
        print(f"{key}: {value}")

    save_summary(fp_output, summary)
    print(f"\nSaved summary to {fp_output}")


if __name__ == "__main__":
    main()