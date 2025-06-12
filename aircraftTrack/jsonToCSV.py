import csv
import json

jsonFile =  "aircraftSurveillance/aircraft_data.json"
with open(jsonFile, 'r') as file:
    data = json.load(file)

fields = ['hex', 'type', 'r', 't', 'dbFlags', 'desc', 'alt_baro', 
'alt_geom', 'gs', 'track', 'squawk', 'lat', 'lon', 
'nic' , 'rc' , 'seen_pos' , 'nac_p', 'nac_v', 
'sil', 'sil_type', 'alert', 'spi', 'mlat', 'tisb',
'messages', 'seen', 'rssi']


rows = []
for aircraft in data['ac']:
    row = []
    for field in fields:
        val = aircraft.get(field, 0)
        if field in ['lat', 'lon'] and val is None:
            val = 0
        row.append(val)
    rows.append(row)

with open("aircraftSurveillance/aircraft_data.csv", "w", newline="") as f:
    fileWriter = csv.writer(f)
    fileWriter.writerow(fields)
    fileWriter.writerows(rows)

