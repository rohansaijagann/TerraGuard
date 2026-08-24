"""
"Krishi Yanthradhare" Karnataka Farm Machinery & Drone Custom Hiring Centre (CHC) Locator.
Provides spatial lookup to the nearest government-subsidized farm mechanization hubs:
- GPS locator to nearest Krishi Yanthradhare CHC depot
- Subsidized hourly rental tariffs vs private market benchmark rates
- Agriculture Drone Spraying (Foliar/Fertilizer/Pesticide) booking information
"""

import math

# Karnataka State Krishi Yanthradhare CHC Centers Directory across Key Hubs
KARNATAKA_CHC_CENTRES = [
    {"name": "Krishi Yanthradhare CHC Hub - Mandya", "district": "Mandya", "taluk": "Mandya Rural", "lat": 12.5280, "lon": 76.8920, "phone": "+91 8232 224501", "address": "RSK Complex, Mandya-571401", "operator": "Karnataka Agri Machinery Corporation / SKDRDP"},
    {"name": "Krishi Yanthradhare CHC Centre - Mysuru", "district": "Mysuru", "taluk": "Mysuru South", "lat": 12.2850, "lon": 76.6450, "phone": "+91 821 2445602", "address": "Agri Bhavan Road, Mysuru-570008", "operator": "Dept. of Agriculture / SKDRDP"},
    {"name": "Krishi Yanthradhare Hub - Tumakuru", "district": "Tumakuru", "taluk": "Tumakuru Central", "lat": 13.3420, "lon": 77.1080, "phone": "+91 816 2289401", "address": "B.H. Road, Tumakuru-572102", "operator": "SKDRDP Krishi Yanthradhare"},
    {"name": "Krishi Yanthradhare CHC - Kolar", "district": "Kolar", "taluk": "Kolar Town", "lat": 13.1410, "lon": 78.1310, "phone": "+91 8152 227801", "address": "APMC Yard Road, Kolar-563101", "operator": "CHC Kolar Farmers Trust"},
    {"name": "Krishi Yanthradhare CHC - Chikkamagaluru", "district": "Chikkamagaluru", "taluk": "Mudigere / Chikkamagaluru", "lat": 13.3180, "lon": 75.7690, "phone": "+91 8262 231502", "address": "Kadur Bypass, Chikkamagaluru-577102", "operator": "Horticulture Mechanization Cell"},
    {"name": "Krishi Yanthradhare Hub - Shivamogga", "district": "Shivamogga", "taluk": "Bhadravathi / Shimoga", "lat": 13.9350, "lon": 75.5720, "phone": "+91 8182 228910", "address": "Sagar Main Road, Shivamogga-577201", "operator": "SKDRDP Agro-Services"},
    {"name": "Krishi Yanthradhare CHC - Belagavi", "district": "Belagavi", "taluk": "Gokak / Belagavi", "lat": 15.8550, "lon": 74.5020, "phone": "+91 831 2419801", "address": "Khanapur Road, Belagavi-590006", "operator": "Belagavi Krishi Sangha"},
    {"name": "Krishi Yanthradhare Hub - Kalaburagi", "district": "Kalaburagi", "taluk": "Kalaburagi North", "lat": 17.3380, "lon": 76.8390, "phone": "+91 8472 254101", "address": "Sedam Ring Road, Kalaburagi-585105", "operator": "Dryland Mechanization Board"},
    {"name": "Krishi Yanthradhare CHC - Ballari", "district": "Ballari", "taluk": "Siruguppa / Ballari", "lat": 15.1450, "lon": 76.9280, "phone": "+91 8392 279502", "address": "Hospet Road, Ballari-583104", "operator": "SKDRDP Machinery Trust"},
    {"name": "Krishi Yanthradhare CHC - Raichur", "district": "Raichur", "taluk": "Sindhanur / Raichur", "lat": 16.2100, "lon": 77.3590, "phone": "+91 8532 229101", "address": "Station Road, Raichur-584102", "operator": "TBP Command Area Mechanization"},
    {"name": "Krishi Yanthradhare CHC - Davanagere", "district": "Davanagere", "taluk": "Harihar / Davanagere", "lat": 14.4690, "lon": 75.9280, "phone": "+91 8192 235601", "address": "PB Road, Davanagere-577006", "operator": "Davanagere Agri Depot"},
    {"name": "Krishi Yanthradhare CHC - Hassan", "district": "Hassan", "taluk": "Hassan Rural", "lat": 13.0110, "lon": 76.1050, "phone": "+91 8172 269401", "address": "BM Road, Hassan-573201", "operator": "SKDRDP Hassan"},
    {"name": "Krishi Yanthradhare CHC - Mangaluru", "district": "Dakshina Kannada", "taluk": "Bantwal / Mangaluru", "lat": 12.8750, "lon": 74.8490, "phone": "+91 824 2439101", "address": "BC Road, Bantwal-574211", "operator": "Coastal Plantation Mechanization"},
    {"name": "Krishi Yanthradhare CHC - Bagalkot", "district": "Bagalkot", "taluk": "Jamkhandi / Bagalkot", "lat": 16.1750, "lon": 75.6690, "phone": "+91 8354 237801", "address": "Navanagar, Bagalkot-587103", "operator": "UAS Dharwad CHC Extension"},
    {"name": "Krishi Yanthradhare CHC - Kodagu", "district": "Kodagu", "taluk": "Somwarpet / Madikeri", "lat": 12.4280, "lon": 75.7420, "phone": "+91 8272 229601", "address": "College Road, Madikeri-571201", "operator": "Hill Agro Mechanization Centre"}
]

# Standard Subsidized Machinery Hiring Catalog
SUBSIDIZED_MACHINERY_CATALOG = [
    {"equipment": "Agriculture Drone Spraying Unit (10L / 16L)", "equipment_kn": "ಕೃಷಿ ಡ್ರೋನ್ ಸಿಂಪಡಣೆ ಘಟಕ (೧೦ ಲೀ / ೧೬ ಲೀ)", "chc_rate": "₹350 / acre", "market_rate": "₹750 / acre", "savings": "53% Subsidized", "use_case": "Nano-Urea, Micronutrient & Bio-fungicide aerial spray in 8 mins/acre"},
    {"equipment": "4WD 50HP Farm Tractor + Plough", "equipment_kn": "೪-ವೀಲ್ ಡ್ರೈವ್ ೫೦HP ಟ್ರ್ಯಾಕ್ಟರ್ + ನೇಗಿಲು", "chc_rate": "₹450 / hour", "market_rate": "₹900 / hour", "savings": "50% Subsidized", "use_case": "Deep summer ploughing & hardpan shattering"},
    {"equipment": "Rotary Tiller / Rotavator (6 Feet)", "equipment_kn": "ರೋಟಾವೇಟರ್ (೬ ಅಡಿ)", "chc_rate": "₹520 / hour", "market_rate": "₹1,100 / hour", "savings": "52% Subsidized", "use_case": "Secondary tillage & clod pulverization for fine seedbed"},
    {"equipment": "Self-Propelled Paddy Transplanter (4/6 Row)", "equipment_kn": "ಭತ್ತ ನಾಟಿ ಯಂತ್ರ (೪/೬ ಸಾಲು)", "chc_rate": "₹1,200 / acre", "market_rate": "₹2,600 / acre", "savings": "54% Subsidized", "use_case": "Precision geometric paddy seedling transplantation"},
    {"equipment": "Multi-Crop Combine Harvester", "equipment_kn": "ಬಹು-ಬೆಳೆ ಕಟಾವು ಯಂತ್ರ", "chc_rate": "₹1,800 / hour", "market_rate": "₹3,400 / hour", "savings": "47% Subsidized", "use_case": "Simultaneous harvesting, threshing & grain bagging (Paddy, Maize, Soybean)"},
    {"equipment": "Laser Land Leveller", "equipment_kn": "ಲೇಸರ್ ಭೂ ಸಮತಟ್ಟು ಯಂತ್ರ", "chc_rate": "₹600 / hour", "market_rate": "₹1,250 / hour", "savings": "52% Subsidized", "use_case": "Zero-gradient leveling to reduce irrigation water wastage by 35%"}
]

def locate_nearest_chc_machinery(lat=13.0, lon=77.0):
    """
    Finds the nearest Krishi Yanthradhare CHC center and returns machinery hiring catalog.
    """
    def haversine(lat1, lon1, lat2, lon2):
        R = 6371.0
        phi1, phi2 = math.radians(lat1), math.radians(lat2)
        dphi = math.radians(lat2 - lat1)
        dlambda = math.radians(lon2 - lon1)
        a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
        return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    centres_with_dist = []
    for c in KARNATAKA_CHC_CENTRES:
        dist = haversine(lat, lon, c["lat"], c["lon"])
        centres_with_dist.append({**c, "distance_km": round(dist, 1)})

    centres_with_dist.sort(key=lambda x: x["distance_km"])
    nearest = centres_with_dist[0]

    return {
        "chc_name": nearest["name"],
        "district": nearest["district"],
        "taluk": nearest["taluk"],
        "distance_km": nearest["distance_km"],
        "phone": nearest["phone"],
        "address": nearest["address"],
        "operator": nearest["operator"],
        "machinery_catalog": SUBSIDIZED_MACHINERY_CATALOG,
        "booking_portal": "https://raitamitra.karnataka.gov.in",
        "toll_free_kisan_call_center": "1800-425-3553 / 1551"
    }
