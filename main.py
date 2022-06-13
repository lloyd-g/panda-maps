#https://www.analyticsvidhya.com/blog/2021/09/how-to-visualise-data-in-maps-using-geopandas/
import geopandas as gpd
import matplotlib.pyplot as plt



#https://geopandas.org/en/stable/docs/user_guide/mapping.html
#plt.show()
import urllib.request
import json
from mpl_toolkits.mplot3d import Axes3D

from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
# Let's then open the data we got (it acts like a file) and get the data
url = 'https://services.swpc.noaa.gov/json/ovation_aurora_latest.json'
req = urllib.request.urlopen(url).read().decode()

# The we can load the json recived from the call
data = json.loads(req)
# Print the data to view it
#"Observation Time": "2022-06-08T08:01:00Z", "Forecast Time": "2022-06-08T09:22:00Z", "Data Format": "[Longitude, Latitude, Aurora]", "coordinates":
print(data['Observation Time'])
print(data['Forecast Time'])
print(data['Data Format'])
#print(data['coordinates'])

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax = fig.add_subplot(111)
#ax = world["geometry"].boundary.plot(figsize=(20,16))
#world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
#ax = world.plot(figsize=(10,6))
fig, ax = plt.subplots(figsize=[14,6])
df = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
df.plot(ax=ax)
x =[]
y =[]
z =[]
for points in data['coordinates']: 
  #print(points)
  if points[0] > 180 :
    x.append((points[0])-360)
  else:
    x.append(points[0])
  y.append(points[1])
  z.append(points[2])
print(max(z)) 
print(min(z))

#ax.world.boundary.plot();
ax.scatter(x, y, z, marker='o',cmap='hot',c=z)

ax.azim = 90
ax.dist = 10
ax.elev = 80
ax.roll = 30
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('Aurora at '+data['Forecast Time'])
plt.xlim( [-180, 180 ] )          # Plot from x=0 to x=80.
plt.ylim( [ -90, 90 ] )         # Plot from y=0 to y=250.
plt.xticks( range(-180,180,30) )   # Put x axis ticks every 10 units.
plt.yticks( range(-90,90,10) )  # Y ticks every 50.  You can provide any list.
plt.show()
