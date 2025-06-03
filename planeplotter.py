import folium
import pandas as pd


print(folium.__version__)
df = pd.read_csv("aircraftSurveillance/aircraft_data.csv")

# sample code to test map thing for folium
m = folium.Map(location=(45.5236, -122.6750), max_bounds=True)
m.save("aircraftSurveillance/aircraft_plot.html")

