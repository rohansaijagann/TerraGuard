import requests, json, os, time
OUTPUT = "d:/MAJORPROJ/terraguard/decision_support/static/geojson/karnataka_forests.geojson"
STRIPS = [
    (11.5, 74.0, 13.2, 76.5, "South"),
    (12.8, 74.0, 14.5, 76.5, "South-Central"),
    (14.0, 74.0, 15.8, 76.5, "Central"),
    (15.3, 74.0, 17.0, 76.5, "North"),
    (16.5, 74.0, 18.5, 76.5, "Far North"),
    (11.5, 76.3, 18.5, 78.6, "East"),
]
all_features = []
seen_ids = set()
for (s, w, n, e, label) in STRIPS:
    query = f'[out:json][timeout:30];(way["natural"="wood"]({s},{w},{n},{e});way["landuse"="forest"]({s},{w},{n},{e}););out geom;'
    print(f"Fetching {label}...", end=" ", flush=True)
    try:
        r = requests.post("https://overpass-api.de/api/interpreter", data={"data": query}, headers={"User-Agent": "TerraGuard/1.0"}, timeout=35)
        if r.status_code == 200:
            count = 0
            for el in r.json().get("elements", []):
                eid = el.get("id")
                if eid in seen_ids or el["type"] != "way" or not el.get("geometry"): continue
                pts = [[p["lon"], p["lat"]] for p in el["geometry"]]
                if len(pts) < 3: continue
                if pts[0] != pts[-1]: pts.append(pts[0])
                seen_ids.add(eid)
                name = (el.get("tags") or {}).get("name") or "Karnataka Forest"
                c_lat = sum(p[1] for p in pts) / len(pts)
                c_lon = sum(p[0] for p in pts) / len(pts)
                all_features.append({"type":"Feature","properties":{"name":name,"center_lat":c_lat,"center_lon":c_lon},"geometry":{"type":"Polygon","coordinates":[pts]}})
                count += 1
            print(f"{count} polygons")
        else:
            print(f"HTTP {r.status_code}")
    except Exception as e:
        print(f"ERROR: {e}")
    time.sleep(1)
print(f"Total: {len(all_features)} polygons")
os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
with open(OUTPUT, "w") as f:
    json.dump({"type":"FeatureCollection","features":all_features}, f)
print("Saved!")
