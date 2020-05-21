{"type": "Polygon", 
 "coordinates": [[
   [-102.05, 41.0], 
   [-102.05, 37.0], 
   [-109.05, 37.0], 
   [-109.05, 41.0]
 ]]}

co = {"type": "Polygon", "coordinates": [
    [(-102.05, 41.0),
     (-102.05, 37.0),
     (-109.05, 37.0),
     (-109.05, 41.0)]]}
lon, lat = zip(*co['coordinates'][0])
print(lon, lat)
from pyproj import Proj
pa = Proj("+proj=aea +lat_1=37.0 +lat_2=41.0 +lat_0=39.0 +lon_0=-105.55")

x, y = pa(lon, lat)

print(x,y)
cop = {"type": "Polygon", "coordinates": [zip(x, y)]}
from shapely.geometry import shape
print(shape(cop).area)  # 268952044107.43506
print(shape(cop).centroid)
