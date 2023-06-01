import osmnx as ox
import matplotlib.pyplot as plt

# Specify the name that is used to seach for the data
place_name = "Kamppi, Helsinki, Finland"

# Fetch OSM street network from the location
graph = ox.graph_from_place(place_name)
type(graph)


# Retrieve buildings from the area
buildings = ox.plot_footprints(place_name)

# What types are those?
print(type(buildings))