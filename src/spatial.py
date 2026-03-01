from shapely.geometry import Point as ShapelyPoint
from shapely.geometry import Polygon as ShapelyPolygon
from math import cos, radians

class SpatialObject:
    """
    Base class for anything that exists in space.
    Stores geometry and provides shared spatial behavior.
    """

    def __init__(self, geometry):
        self.geometry = geometry

    def area(self):
        """
        Approximate area in square meters for geographic coordinates.
        """
        if self.geometry.area == 0.:
            return 0
        
        lat = self.geometry.centroid.y

        # Convert from geographic coordinates to projected coordinates
        meters_per_degree_latitude = 111320
        meters_per_degree_longitude = meters_per_degree_latitude * cos(radians(lat))

        area = self.geometry.area * meters_per_degree_latitude * meters_per_degree_longitude
        return area

class Parcel(SpatialObject):
    """
    Parcel = spatial object + structured attributes.
    """

    def __init__(self, parcel_id: int, geometry: dict, zone: str, is_active: bool, area_sqm: float):
        
        self.geometry_type = "Polygon"
        self.geometry_coords = geometry["coordinates"]
        self.shell = geometry["coordinates"][0]

        if len(geometry["coordinates"]) > 1:
            self.holes = [i for i in geometry["coordinates"][1:]]
        else:
            self.holes = None
        
        if geometry["type"] == self.geometry_type:
            polygon = ShapelyPolygon(self.shell, self.holes)
            super().__init__(polygon)
        else:
            raise TypeError("Parcel geometry must be `Polygon`.")
        
        self.id = parcel_id
        self.zone = zone
        self.is_active = is_active
        self.area_sqm = area_sqm

    @classmethod
    def from_dict(cls, d: dict):
        return cls(**d)
    
    def as_dict(self):
        return {
            "parcel_id": self.id,
            "zone": self.zone,
            "is_active": self.is_active,
            "area_sqm": self.area(),
            "geometry": {
                "type": self.geometry_type,
                "coordinates": self.geometry_coords
            }
        }
        
