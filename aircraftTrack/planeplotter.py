import folium
import pandas as pd
import random

df = pd.read_csv("aircraftSurveillance/aircraft_data.csv")

color_list = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 'lightred',
 'beige', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple', 
 'white', 'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray']


map = folium.Map(location=(40, -100), max_bounds=True, zoom_start= 4)
# figure out how to make markers from csv
for index, row in df.iterrows():
    if row['lat'] != 0 and row['lon'] != 0 and row['hex'].lower().startswith('a'):
        html=f"""
            <b>Callsign:</b> {row['r']} <br>
            <b>Type:</b> {row['desc']}<br>
            <b>Hex:</b> {row['hex']}<br>
            <b>Altitude:</b> {row['alt_baro']} ft<br>
            <b>Speed:</b> {row['gs']} kt<br>
            <b>Heading:</b> {row['track']}°
        """
        iframe = folium.IFrame(html=html, width=250, height=150)
        popup = folium.Popup(iframe, max_width=300)
        col = random.choice(color_list)
        folium.Marker(
            location=[row['lat'], row['lon']],
            popup=popup,
            icon=folium.Icon(color=col, icon="arrow-up", prefix='fa', angle=row['track'])
        ).add_to(map)



map.save("aircraftSurveillance/aircraft_plot.html")


