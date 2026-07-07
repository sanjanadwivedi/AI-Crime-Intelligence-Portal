import json

features = []

with open("LGD_States.geojsonl", "r", encoding="utf-8") as f:
    for line in f:
        features.append(json.loads(line))

geojson = {
    "type": "FeatureCollection",
    "features": features
}

with open("LGD_States.geojson", "w", encoding="utf-8") as f:
    json.dump(geojson, f, ensure_ascii=False)

print("Conversion completed!")