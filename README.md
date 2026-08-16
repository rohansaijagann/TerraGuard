# 🌱 TerraGuard AI — Digital Twin Climate Decision Support & Ecological Agriculture Platform

> **A Spatial AI-Powered Decision Support Engine for Precision Agroforestry, Satellite Drought Diagnostics, Wildfire Propagation Modeling, and Live Crop Disease Forecasting across Karnataka.**

---

## 📌 Executive Summary

**TerraGuard AI** is an end-to-end Geo-Spatial & Ecological Decision Support Platform tailored specifically to the diverse agro-climatic zones of **Karnataka, India** (Coastal Karavali, Western Ghats / Malenadu, Northern Dry Maidan, and Southern Transition Zone). 

By integrating **live satellite telemetry, real-time meteorological feeds (Open-Meteo), SoilGrids ISRIC global soil databases, and multi-criteria Analytic Hierarchy Process (AHP) algorithms**, TerraGuard empowers farmers, agronomists, and disaster response teams to make climate-resilient decisions.

---

## 🏛️ Platform Architecture

```text
 ┌────────────────────────────────────────────────────────────────────────────────────────┐
 │                                   USER INTERFACE                                       │
 │     Interactive Map (Leaflet.js)  │  Bilingual Panel (EN/KN)  │  Voice Audio Readout   │
 └───────────────────────────────────────────┬────────────────────────────────────────────┘
                                             │ REST API (JSON)
                                             ▼
 ┌────────────────────────────────────────────────────────────────────────────────────────┐
 │                             TERRAGUARD DJANGO REST SUITE                               │
 ├──────────────────────────┬──────────────────────────┬──────────────────────────────────┤
 │  🌾 RecommendationAPI    │   🛰️ DiagnosticsAPI     │   🔥 FireRiskAPI                 │
 │  • AHP Species Ranking   │   • 9-Mo NDVI Tracking   │   • Canadian FWI Index           │
 │  • 4-Tier Agroforestry   │   • Soil Moisture Index  │   • Huygens Elliptic Dispersion  │
 │  • Carbon Sink Credit    │   • Emergency Water Svc  │   • KFD & KSFES Direct Dispatch  │
 ├──────────────────────────┴──────────────────────────┴──────────────────────────────────┤
 │  🔬 PestDiseaseAPI: 42-Disease Live Agro-Ecological Diagnostic Engine                  │
 └───────────────────────────────────────────┬────────────────────────────────────────────┘
                                             │
                                             ▼
 ┌────────────────────────────────────────────────────────────────────────────────────────┐
 │                              EXTERNAL TELEMETRY & DATA                                 │
 │   Open-Meteo Live API  │  SoilGrids ISRIC  │  OSM Overpass  │  Karnataka GIS Polygons  │
 └────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🚀 The 4 Core Intelligence Modules

### 1. 🌾 Precision Agroforestry & Multi-Tier Crop Decision Support
* **Multi-Criteria AHP Optimization**: Evaluates live rainfall ($40\%$), altitude/elevation ($30\%$), soil pH ($20\%$), and carbon sequestration capacity ($10\%$) against an authentic database of **167 Karnataka crops, fruit orchards, spices, floriculture, and timber species**.
* **4-Tier Vertical Canopy Synergy**: Synthesizes 4-layer polyculture designs (*Emergent Timber $\rightarrow$ Fruit Trees $\rightarrow$ Climbing Spice Vines $\rightarrow$ Ground Rhizomes/Millets*) yielding up to **+2.8x farm revenue** (₹3,40,000/acre/yr) while saving $38\%$ water through canopy shading.
* **Crop Sowing Calendar**: Live month-by-month phenological tracking (*Sowing Window Active*, *Vegetative Growth*, *Harvest Ready*).
* **Government Subsidies & Schemes**: Automated matching with **KMSDS** (Spices), **MIDH** (Horticulture), **KAPY** (Tree Plantation DBT), **Raitha Siri** (Millets), and **PMKSY** (Micro-Drip $90\%$ Aid).

### 2. 🛰️ Satellite Drought Monitoring & Early-Warning Diagnostics
* **Live NDVI & Vegetation Health**: Computes 9-month historical and forecasted NDVI trends to detect systemic vegetation degradation.
* **Volumetric Soil Moisture**: Evaluates root-zone moisture anomalies and consecutive dry-day stress levels.
* **Emergency Water Resources**: Queries OpenStreetMap Overpass live to locate and navigate to the nearest surface water reservoir or irrigation canal.
* **Regional Monitoring Stations**: 26 real-time monitoring beacons covering all Karnataka districts (Kalaburagi, Vijayapura, Ballari, Haveri, Shivamogga, Kodagu, Udupi, etc.).

### 3. 🔥 Wildfire Susceptibility & 24h Downwind Dispersion Simulator
* **Dual-Phase Fire Weather Index (FWI)**: Evaluates live ambient temperature, relative humidity, wind speed, and fuel dryness over **20 Protected Forest Reserves & Tiger Reserves** (Bandipur, Nagarahole, Kali, Bhadra, Kudremukh, BRT, Pushpagiri, etc.).
* **Elliptic Huygens Spread Modeling**: Simulates 24-hour fire spread polygons oriented along live wind vector azimuths.
* **First-Responder Integration**: Computes real-time Haversine distance, compass bearing, and travel ETA to the nearest **Karnataka Forest Department (KFD) Range Forest Officer (RFO)** and **KSFES Fire Station** with one-tap emergency calling.

### 4. 🔬 42-Disease Live Crop Diagnostic & Bio-Control Advisor
* **100% Live Meteorological Triggers**: Continuously tests live weather parameters ($T, RH, R_{7d}, W, T_{dew}$) against authentic Karnataka pathology rules:
  * **Plantation & Spices**: Arecanut Koleroga (*Phytophthora meadii*), Yellow Leaf Disease, Anabe Roga (*Ganoderma*), Coconut Bud Rot, Coffee Rust (*Hemileia*), Coffee White Stem Borer, Pepper Quick Wilt, Cardamom Azhukal.
  * **Spices & Condiments**: Ginger/Turmeric Rhizome Soft Rot, Ginger Bacterial Wilt, Cashew Tea Mosquito Bug, Betelvine Foot Rot.
  * **Cereals & Millets**: Rice/Ragi Blast (*Magnaporthe*), Paddy Brown Spot, Stem Borer & BPH, Fall Armyworm (*Spodoptera frugiperda*), Maize Turcicum Blight, Jowar Grain Mold.
  * **Cash Crops**: Bt Cotton Pink Bollworm, Cotton Black Arm, Cotton Grey Mildew (Dahiya), Sugarcane Red Rot, Sugarcane Woolly Aphid.
  * **Pulses & Oilseeds**: Groundnut Tikka & Rust, Soybean Asian Rust, Tur Fusarium Wilt, Tur SMD Mite, Bengal Gram Wilt, Sunflower Alternaria Blight.
  * **Fruits & Vegetables**: Pomegranate Telya Blight (*Xanthomonas*), Grape Downy Mildew (*Plasmopara 3-10 rule*), Mango Blossom Blight, Banana Sigatoka, Citrus Canker, Tomato Early/Late Blight, Chilli Anthracnose, Onion Purple Blotch, Brinjal Shoot Borer.
* **Integrated Pest Management (IPM)**: Provides biological controls (Trichoderma, Pseudomonas, Neem formulations, Beauveria) alongside exact chemical molecules and dilution dosages.
* **🔊 Voice Speech Readout (Kannada & English)**: Built-in text-to-speech advisory for rural accessibility.
* **Emergency Agricultural Centers**: Instant lookup of nearest **Karnataka State Department of Agriculture (KSDA)** Plant Health Clinics and **KSSC Seed Depots**.

---

## 🗂️ Project Structure

```bash
MAJORPROJ/
├── terraguard/
│   ├── manage.py                          # Django management CLI
│   ├── db.sqlite3                         # Seeded SQLite database (167 species)
│   ├── populate_species.py                # Database population script
│   ├── terraguard/
│   │   ├── settings.py                    # Django configuration & API keys
│   │   ├── urls.py                        # Root URL routing
│   │   └── wsgi.py
│   ├── decision_support/
│   │   ├── models.py                      # KarnatakaAgroZone & SpeciesConstraint models
│   │   ├── views.py                       # Recommendation, Diag, Fire, & Pest APIs
│   │   ├── urls.py                        # API route declarations
│   │   ├── ml_utils/
│   │   │   ├── ahp_engine.py              # AHP multi-criteria scoring
│   │   │   └── data_fetcher.py            # Live Open-Meteo & SoilGrids integration
│   │   ├── templates/decision_support/
│   │   │   └── dashboard.html             # Glassmorphism UI, Leaflet map, & speech engine
│   │   └── static/
│   │       ├── css/                       # Leaflet & FontAwesome stylesheets
│   │       ├── js/                        # Turf.js, Chart.js, & Leaflet Draw
│   │       └── geojson/                   # Karnataka state & forest GeoJSON polygons
├── requirements.txt                       # Python dependencies
├── .gitignore                             # Git ignore rules
└── README.md                              # Project documentation
```

---

## 🛠️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Backend Framework** | Python 3.11, Django 5.x, Django REST Framework (DRF) |
| **Frontend & UI** | Vanilla JS (ES6+), Glassmorphism Design System, CSS3 Variables, Google Fonts (Plus Jakarta Sans) |
| **Mapping & GIS** | Leaflet.js 1.9.4, Turf.js (geospatial analysis), Leaflet Draw, GeoJSON |
| **Charts & Visuals** | Chart.js 4.4 |
| **Live Telemetry APIs** | Open-Meteo Weather API, SoilGrids (ISRIC), OpenStreetMap Overpass API |
| **Voice & Accessibility**| HTML5 Web Speech Synthesis API (`kn-IN` & `en-IN`) |
| **Database** | SQLite (Production-ready with Django ORM) |

---

## ⚡ Quickstart & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/rohansaijagann/TerraGuard.git
cd TerraGuard
```

### 2. Set Up Python Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Initialize Database & Seed Species
```bash
cd terraguard
python manage.py migrate
python populate_species.py
```

### 4. Run the Development Server
```bash
python manage.py runserver
```

Open your browser and navigate to: **`http://127.0.0.1:8000/`**

---

## 📡 REST API Reference

| Method | Endpoint | Description | Payload Example |
| :--- | :--- | :--- | :--- |
| `POST` | `/api/recommend/` | Returns top 50 ranked crops/trees, 4-tier agroforestry, & subsidies for coordinates. | `{"latitude": 13.3153, "longitude": 75.7754}` |
| `POST` | `/api/diagnostics/` | Runs satellite drought, NDVI trend, soil moisture, & emergency water scan. | `{"latitude": 17.3297, "longitude": 76.8343}` |
| `POST` | `/api/fire-risk/` | Computes Canadian FWI score, 24h spread ellipse, & nearest KFD/KSFES dispatch stations. | `{"latitude": 11.6664, "longitude": 76.6293}` |
| `POST` | `/api/pest-disease/` | Live 42-disease meteorological diagnostic & nearest KSDA clinic lookup. | `{"latitude": 14.7946, "longitude": 75.4011}` |

---

## 🌐 Bilingual Support (ಕನ್ನಡ & English)

TerraGuard features zero-latency dynamic translation between **English** and **Kannada (ಕನ್ನಡ)** covering all technical metrics, crop names, agroforestry explanations, biological mechanisms, and government schemes.

---

## 📄 License

This project is developed as an academic and open-source initiative for climate-smart agriculture and environmental preservation in Karnataka.

---

**Built with ❤️ for Karnataka Farmers & Forest Protectors by Rohan**
