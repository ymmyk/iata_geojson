import csv
import json


CSV_PATH = "potential_airports.csv"
OUT_PATH = "geojson.json"


def load_data():
    records = []
    with open(CSV_PATH, 'r') as infile:
        reader = csv.reader(infile)
        first = next(reader)
        first[0] = 'id'
        for line in reader:
            records.append(dict(zip(first, line)))

    return records


if __name__ == '__main__':
    data = load_data()
    # Output the points for geojson
    output = {
        "type": "FeatureCollection",
        "features": []
    }
    for record in data:
        # insert map pins for each airport
        output['features'].append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [float(record['longitude_deg']), float(record['latitude_deg'])]
            },
            "properties": {
                "name": record['name'],
                "type": record['type'],
                "country": record['iso_region'],
                "iata_code": record['iata_code'],
                "elevation": record['elevation_ft'],
                "gps_code": record['gps_code'],
                "marker-color": "#7e7e7e" if record['type'] == 'medium_airport' else "#ff0000",
            }
        })
    with open(OUT_PATH, 'w') as outfile:
        json.dump(output, outfile, indent=2)
