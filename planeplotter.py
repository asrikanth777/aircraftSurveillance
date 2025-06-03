import folium
import pandas as pd


print(folium.__version__)
df = pd.read_csv("aircraftSurveillance/aircraft_data.csv")

map = folium.Map(location=(40.1020, -88.2272), max_bounds=True)
# figure out how to make markers from csv



map.save("aircraftSurveillance/aircraft_plot.html")

