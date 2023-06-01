import geocoder
from postal.parser import parse_address
parse_address('The Book Club 100-106 Leonard St Shoreditch London EC2A 4RH, United Kingdom')
parse_address('70b Hauptstraße, Sassnitz, Mecklenburg-Vorpommern 18546 Germansy')

g = geocoder.osm([45.15, -75.14], method='reverse')
print(g.city)
print(g.state)

#g2 = geocoder.osm("3200 S Las Vegas Blvd Space 7500, Las Vegas, NV 89109, United States")
#g2 = geocoder.osm("11 Wall St, New York, NY 10005, USA")
g2 = geocoder.osm("70b Hauptstraße Sassnitz Mecklenburg-Vorpommern 18546 Germany")
g3 = geocoder.osm("70b Hauptstraße, Sassnitz, Mecklenburg-Vorpommern 18546 Germansy")

print(g2.x, g2.y)
print(g3.x, g3.y)
