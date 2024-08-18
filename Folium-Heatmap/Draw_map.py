import folium
from folium.plugins import HeatMap
from Get_and_Preprocess_data import *

df = get_table(url='https://en.wikipedia.org/wiki/List_of_Iranian_four-thousanders')

center_lat = df['Latitude'].mean()
center_lon = df['Longitude'].mean()

# first way
map_base = folium.Map(location=[center_lat, center_lon], zoom_start=6)
HeatMap(df[['Latitude', 'Longitude']]).add_to(map_base)
map_base.save("heatmap.html")


# second way
map_base = folium.Map(location=[center_lat, center_lon], zoom_start=5)
for idx, row in df.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['Persian name']).add_to(map_base)
map_base.save("marker_map.html")