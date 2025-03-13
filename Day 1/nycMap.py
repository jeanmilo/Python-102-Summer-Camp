# Name: Dia Yamamoto
# Purpose: we are going to use the pandas and folium libraries to create a map of NYC !! :D

import folium 
import pandas as pd

# let's make our map focus on the places we want pinned 
places = pd.read_csv("mapData.csv")
print(places["Name"])

#creation of map
mapWorld = folium.Map(location = [40.7128, -74.0060], zoom_start = 10)

# for every item in each row in csv file
for index,row in places.iterrows():
  lat = row[" Latitude"] # looks for value in the Latitude category
  lon = row[" Longitude"] # looks for value in the Longitude category
  name = row["Name"] # looks for value in the Name category

  #creates new marker for map
  newMarker = folium.Marker([lat,lon], popup=name)
  #adds marker to map
  newMarker.add_to(mapWorld)

# save map as html file so we can look at our map on chrome
mapWorld.save(outfile = "tempMap.html")
