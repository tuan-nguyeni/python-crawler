from OSMPythonTools.nominatim import Nominatim
from OSMPythonTools.overpass import overpassQueryBuilder, Overpass

"""
vienna = Nominatim().query('Vienna, Austria')
query = overpassQueryBuilder(area=vienna.areaId(), elementType=['way', 'relation'], selector='"building"="yes"', includeGeometry=True)
result = Overpass().query(query)
print(result.countElements())
print(result.elements()[0].geometry())
"""

# import osmnx
import osmnx as ox
import geopandas as gpd

place_name = "Liechtenstein"

# Get place boundary related to the place name as a geodataframe
area = ox.geocode_to_gdf(place_name)

tags = {'building': 'commercial'}
#tags = {'amenity': 'atm'}

buildings = ox.geometries_from_place(place_name, tags)
print(buildings.head(10))
#print(buildings.get("node=='2269325371'"))
print(buildings.count())