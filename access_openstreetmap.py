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

place_name = "ingolstadt"
data_path = "data/poi_data/"
prefix = "_poi.csv"
tags_query ="shop"

# Get place boundary related to the place name as a geodataframe
area = ox.geocode_to_gdf(place_name)

tags = {tags_query: True}

amenity = ox.geometries_from_place(place_name, tags)
print(amenity.head(10))
print(amenity.count())

amenity.to_csv(data_path+tags_query+place_name+prefix)