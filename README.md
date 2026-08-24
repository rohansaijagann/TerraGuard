# 🌱 TerraGuard AI — Digital Twin Climate Decision Support & Agro-Economic Intelligence Platform

> **A Comprehensive Geo-Spatial AI Decision Support Engine for Precision Agroforestry, AI Agronomy, Predictive Yield Modeling, Satellite Drought Diagnostics, Wildfire Propagation Simulation, and Rural Financial Intelligence across Karnataka, India.**

---

## 📌 Executive Summary

**TerraGuard AI** is an end-to-end Geo-Spatial, Ecological, and Agro-Economic Decision Support Platform engineered specifically for the diverse agro-climatic zones of **Karnataka, India** (*Coastal Karavali, Western Ghats / Malenadu, Northern Dry Maidan, Central & Southern Transition Zones*).

By fusing **real-time meteorological telemetry (Open-Meteo), SoilGrids ISRIC global soil databases, Central Ground Water Board (CGWB) aquifer telemetry, NASA FIRMS & ISRO Bhuvan satellite thermal feeds, Multi-Criteria Analytic Hierarchy Process (AHP), Google Gemini AI, and Karnataka APMC Mandi trade indexes**, TerraGuard equips farmers, forest conservators, agronomists, and disaster response units with hyper-localized, actionable intelligence.

---

## 🏛️ Platform Architecture

```text
 ┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
 │                                   USER INTERFACE & GLASSMORPHIC HUD                              │
 │   Interactive Leaflet Map  │  Bilingual Panel (EN/KN)  │  Voice WebSpeech (TTS) │  AI Chatbot   │
 └──────────────────────────────────────────────────┬───────────────────────────────────────────────┘
                                                    │ REST API (JSON)
                                                    ▼
 ┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
 │                                    TERRAGUARD DJANGO REST SUITE                                  │
 ├─────────────────────────┬──────────────────────────┬──────────────────────────┬──────────────────┤
 │  🌾 RecommendationAPI   │  🤖 RaithaSahayakaAPI    │  🧪 FertilizerCalcAPI    │  ⚡ AgriPVAPI    │
 │  • 167 Species AHP      │  • Gemini 1.5 + UAS Rule │  • Stoichiometric NPK    │  • PM-KUSUM A    │
 │  • 4-Tier Agroforestry  │  • Voice TTS & Speech-In │  • Commercial Bag Units  │  • Dual Revenue  │
 ├─────────────────────────┼──────────────────────────┼──────────────────────────┼──────────────────┤
 │  📈 APMCMarketAPI       │  🌲 CarbonCreditAPI      │  🚜 MachineryRentalAPI   │  🛡️ PMFBYAPI     │
 │  • 17 Mandi Yard Feeds  │  • Verra 20-Yr Biomass   │  • Krishi Yanthradhare   │  • Scale of Fin. │
 │  • 3-Month Price Trend  │  • VCM Monetization      │  • Drone Rental (₹350/ac)│  • Loss Triggers │
 ├─────────────────────────┼──────────────────────────┼──────────────────────────┼──────────────────┤
 │  🌾 YieldEstimatorAPI   │  🛰️ DiagnosticsAPI      │  🔥 FireRisk & Thermal   │  🔬 PestDisease  │
 │  • ML Yield Regressor   │  • 9-Month NDVI & SPI    │  • Rothermel Huygens     │  • 42 Pathology  │
 │  • Organic/Precision Scn│  • CGWB Aquifer Depth    │  • NASA FIRMS Hotspots   │  • KSDA Clinics  │
 └─────────────────────────┴──────────────────────────┴──────────────────────────┴──────────────────┤
                                                    │
                                                    ▼
 ┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
 │                                   EXTERNAL TELEMETRY & DATABASES                                 │
 │   Open-Meteo Live API  │  ISRIC SoilGrids  │  CGWB Aquifer  │  NASA FIRMS  │  Karnataka GIS      │
 └──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Core Intelligence Modules

### 1. 🌾 Precision Agroforestry & 4-Tier Canopy Optimization
* **Multi-Criteria AHP Optimization**: Evaluates live rainfall ($40\%$), altitude/elevation ($30\%$), soil pH ($20\%$), and carbon sequestration capacity ($10\%$) against an authentic database of **167 Karnataka crops, fruit orchards, spices, floriculture, and timber species**.
* **4-Tier Vertical Canopy Synergy**: Synthesizes 4-layer polyculture designs (*Emergent Timber $\rightarrow$ Fruit Trees $\rightarrow$ Climbing Spice Vines $\rightarrow$ Ground Rhizomes/Millets*) yielding up to **+2.8x farm revenue** (₹3,40,000/acre/yr) while saving $38\%$ water through canopy shading.
* **Crop Sowing Calendar**: Live month-by-month phenological tracking (*Sowing Window Active*, *Vegetative Growth*, *Harvest Ready*).

---

### 2. 🤖 "Raitha Sahayaka" AI Conversational Agronomist (100% Free)
* **Dual-Engine Intelligence**:
  * **Google Gemini 1.5 Flash**: Powered by Google AI Studio's **Free Tier** (15 RPM / 1,500 RPD) for open-ended agronomic queries.
  * **Built-in Karnataka Agronomic Expert Engine**: Pre-calibrated rules from **UAS Bengaluru & UAS Dharwad** providing **100% free, offline, instant** answers for fertilizers, water management, spacing, and subsidies.
* **Farm-Grounded Telemetry**: Automatically ingests clicked farm coordinates, soil pH, nitrogen, rainfall, and aquifer depth.
* **🎙️ Voice-First Accessibility**:
  * **Voice Input**: Web Speech Recognition in Kannada (`kn-IN`) and English (`en-IN`).
  * **Audio Readout (TTS)**: Built-in `🔊 Listen / ಕೇಳಿ` button to read advice aloud for rural farmers.

---

### 3. 🧪 Precision Fertilizer & Stoichiometric NPK Dosage Calculator
* **Nutrient Uptake Modeling**: Computes exact $N, P_2O_5, K_2O$ requirements (kg/acre) calibrated for soil pH (correcting for acidic/alkaline phosphate lockup) and organic carbon (SOC).
* **Commercial Bag Conversion**: Translates nutrient deficits into commercial bag units: **Urea (45kg)**, **DAP (50kg)**, and **MOP (50kg)** with Karnataka subsidized DBT pricing.
* **3-Stage Split Application Schedule**: *Basal at sowing*, *Day 30 vegetative stage*, and *Day 60 flowering/grain-filling*.
* **Organic Alternatives**: Calculates Farmyard Manure (FYM) tonnage, vermicompost, and bio-fertilizer packages (*Azospirillum, PSB, Rhizobium*).

---

### 4. ⚡ Solar Agri-Photovoltaics (Agri-PV) Dual-Income Modeler
* **Agrivoltaic Land-Use**: Models 3.5m elevated bifacial solar PV arrays above shade-tolerant crops (*Turmeric, Ginger, Black Pepper, Coffee, Vanilla, Fodder*).
* **Regional Solar Insolation**: Calibrated for Karnataka Global Horizontal Irradiance (GHI 4.85–5.75 $\text{kWh}/\text{m}^2/\text{day}$).
* **PM-KUSUM Component A**: Computes grid export earnings under ESCOM feed-in tariffs (@ ₹3.15/unit), unlocking **3x to 9x gross farm revenue multipliers**.

---

### 5. 📈 Live Karnataka APMC Mandi Market Intelligence
* **Mandi Hub Directory**: Live trade tracking across 17 major Karnataka APMC market yards (*Yeshwantpur, Byadgi Chilli, Kolar Tomato, Tiptur Copra, Shivamogga Arecanut, Raichur Cotton, Kalaburagi Toor, Hubballi, Mysuru, Mandya, Belagavi, Davanagere*).
* **Spatial Rate Calculation**: Computes Haversine distance, freight transport cost per quintal, daily arrival volumes, and modal/min/max spot rates.
* **3-Month Seasonal Price Outlook**: Forecasts festival and harvest price trends.

---

### 6. 🌲 20-Year Carbon Credit Monetization Engine (Verra Standards)
* **Biomass Accumulation Curves**: Implements Verra VM0042 & Gold Standard forestry methodologies for 14 timber species (*Melia Dubia, Bamboo, Teak, Sandalwood, Pongamia, Silver Oak, Rosewood*).
* **Voluntary Carbon Market (VCM)**: Calculates annual and 20-year cumulative $t\text{CO}_2e$ sequestration cashflow @ \$15/credit (₹1,250/credit) with milestone payout tables for Years 1, 5, 10, and 20.

---

### 7. 🚜 "Krishi Yanthradhare" Farm Machinery & Drone Rental Locator
* **Custom Hiring Centre (CHC) Directory**: Locates the nearest Karnataka Government CHC machinery depot.
* **Subsidized Rental Catalog**:
  * **Agriculture Drone Spraying**: ₹350/acre (53% subsidy vs market ₹750/acre)
  * **4WD 50HP Farm Tractor**: ₹450/hr (50% subsidy vs market ₹900/hr)
  * **Rotary Tiller / Rotavator**: ₹520/hr (52% subsidy vs market ₹1,100/hr)
  * **Paddy Transplanter**: ₹1,200/acre (54% subsidy vs market ₹2,600/acre)
  * **Combine Harvester**: ₹1,800/hr (47% subsidy vs market ₹3,400/hr)
* **Direct Booking Access**: Complete with operator contact numbers and application links.

---

### 8. 🛡️ PMFBY Crop Insurance & Risk Coverage Calculator
* **Scale of Finance**: PMFBY Karnataka sum-insured scale database covering 27 agricultural and horticultural crops.
* **Subsidized Farmer Premiums**: **1.5%** for Rabi, **2.0%** for Kharif, and **5.0%** for Commercial/Horticultural crops (with 85%+ government subsidy absorption).
* **Automated Claim Triggers**: Details loss indemnity conditions for monsoon deficits >75%, prevented sowing, and mid-season dry spells >21 days under *Samrakshane Karnataka*.

---

### 9. 🌾 Predictive ML Crop Yield Estimator
* **Agro-Climatic Regression**: Predicts per-acre crop yields (in Quintals/Tons) based on annual precipitation, soil pH, organic carbon, and elevation.
* **Scenario Modeling**: Interactive switch between **Organic Farming**, **Standard Cultivation**, and **High-Input Precision Farming**.

---

### 10. 💧 Central Ground Water Board (CGWB) Aquifer Telemetry
* **31-District Groundwater Monitoring**: Ingests Karnataka CGWB borewell aquifer depth data (meters below ground level - mbgl).
* **Depletion Warnings**: Automatically alerts farmers against high-water footprint crops when aquifer levels fall into *Critical (>30m)* or *Over-Exploited (>45m)* zones.

---

### 11. 🛰️ Satellite Drought Monitoring & Early-Warning Diagnostics
* **Live NDVI & Vegetation Health**: Computes 9-month historical and forecasted NDVI trends to detect systemic vegetation degradation.
* **Standardized Precipitation Index (SPI)**: Evaluates meteorological and agricultural drought severity.
* **Emergency Water Resources**: Queries OpenStreetMap Overpass live to locate and navigate to the nearest surface water reservoir or canal.
* **26-District Regional Scanner**: Real-time monitoring beacons covering all Karnataka districts.

---

### 12. 🔥 Forest Fire Susceptibility & NASA FIRMS Thermal Anomaly Feed
* **Dual-Phase Fire Weather Index (FWI)**: Evaluates live temperature, relative humidity, wind speed, and fuel dryness across 20 Protected Forest & Tiger Reserves (*Bandipur, Nagarahole, Kali, Bhadra, Kudremukh, BRT, Pushpagiri*).
* **Huygens Elliptic Fire Spread**: Simulates 24-hour downwind fire dispersion ellipses along real-time wind vectors.
* **NASA FIRMS & ISRO Bhuvan Hotspot Feed**: Displays real-time satellite infrared thermal anomalies with active fire brightness values.
* **Emergency Dispatch**: Instant Haversine distance, travel ETA, and one-tap emergency calling to the nearest **Karnataka Forest Department (KFD) RFO** and **KSFES Fire Station**.

---

### 13. 🔬 42-Disease Crop Pathology & Bio-Control Advisor
* **100% Live Weather Triggers**: Evaluates live temperature, humidity, and 7-day cumulative rainfall against Karnataka crop disease models (*Arecanut Koleroga, Rice Blast, Grape Downy Mildew, Pomegranate Bacterial Blight, Coffee Rust, Cotton Pink Bollworm*).
* **Integrated Pest Management (IPM)**: Biological treatments (*Trichoderma, Pseudomonas, Neem*) paired with exact chemical active ingredients and dilution rates.
* **Agri-Input Locator**: Haversine distance and contact details for nearest verified agrochemical stores and **KSDA Plant Health Clinics**.

---

## 🗂️ Project Structure

```bash
MAJORPROJ/
├── render.yaml                            # Cloud deployment configuration
├── Procfile                               # Gunicorn web process definition
├── requirements.txt                       # Python dependencies
├── README.md                              # Comprehensive documentation
├── terraguard/
│   ├── manage.py                          # Django management CLI
│   ├── db.sqlite3                         # Seeded SQLite database
│   ├── terraguard/
│   │   ├── settings.py                    # Django configuration & middleware
│   │   ├── urls.py                        # Root URL routing
│   │   └── wsgi.py                        # WSGI entrypoint
│   ├── decision_support/
│   │   ├── models.py                      # KarnatakaAgroZone & SpeciesConstraint models
│   │   ├── views.py                       # All 17 REST API View Controllers
│   │   ├── urls.py                        # API route declarations
│   │   ├── management/
│   │   │   └── commands/
│   │   │       └── seed_data.py           # Production botanical database seeder
│   │   ├── ml_utils/
│   │   │   ├── ahp_engine.py              # AHP multi-criteria scoring algorithm
│   │   │   ├── ai_agronomist.py           # Raitha Sahayaka Gemini & UAS agronomy engine
│   │   │   ├── fertilizer_calculator.py   # Stoichiometric NPK & commercial bag engine
│   │   │   ├── agri_pv_modeler.py         # Solar Agri-PV & PM-KUSUM dual-revenue model
│   │   │   ├── apmc_market_feed.py        # 17 Karnataka APMC Mandi rates & forecast
│   │   │   ├── carbon_credit_engine.py    # Verra 20-year tree biomass sequestration
│   │   │   ├── krishi_machinery_chc.py    # Custom Hiring Centre machinery locator
│   │   │   ├── pmfby_insurance.py         # PMFBY crop insurance & claim trigger engine
│   │   │   ├── groundwater_cgwb.py        # 31-district CGWB aquifer depth telemetry
│   │   │   ├── subsidy_matcher.py         # Karnataka government subsidy scheme engine
│   │   │   ├── geo_validator.py           # Karnataka offline lake & river detector
│   │   │   └── data_fetcher.py            # Open-Meteo & SoilGrids integration
│   │   └── templates/decision_support/
│   │       └── dashboard.html             # Glassmorphism UI, Leaflet Map, & Speech Engine
```

---

## 📡 Complete REST API Reference

| Method | Endpoint | Description | Sample Payload |
| :--- | :--- | :--- | :--- |
| `POST` | `/api/recommend/` | Top-ranked crops, 4-tier canopy layout, fertilizer, APMC rates & subsidies | `{"latitude": 13.3153, "longitude": 75.7754}` |
| `POST` | `/api/raitha-sahayaka/` | Raitha Sahayaka AI conversational agronomy advice (KN/EN) | `{"query": "ಎಕರೆಗೆ ಎಷ್ಟು ಗೊಬ್ಬರ ಹಾಕಬೇಕು?", "language": "kn"}` |
| `POST` | `/api/fertilizer-calc/` | Stoichiometric NPK dosage, commercial bags (Urea/DAP/MOP) & split schedule | `{"species": "Ragi", "latitude": 13.0, "longitude": 77.0, "acres": 2.0}` |
| `POST` | `/api/agri-pv/` | Solar Agri-PV capacity (kWp), generation (kWh), PM-KUSUM revenue & dual return | `{"species": "Turmeric", "latitude": 13.0, "crop_revenue": 180000, "acres": 1.5}` |
| `POST` | `/api/apmc-prices/` | Nearest Karnataka APMC mandi, spot modal price, arrivals & 3-month outlook | `{"species": "Byadgi Chilli", "latitude": 14.68, "longitude": 75.48}` |
| `POST` | `/api/carbon-credits/` | 20-year tree carbon sequestration trajectory ($t\text{CO}_2e$) & VCM cashflow milestones | `{"species": "Melia Dubia", "acres": 2.0, "credit_price_usd": 15}` |
| `POST` | `/api/machinery-rental/`| Nearest Krishi Yanthradhare CHC depot & subsidized rental machinery catalog | `{"latitude": 14.46, "longitude": 75.92}` |
| `POST` | `/api/pmfby-insurance/` | PMFBY sum insured, subsidized farmer premium (1.5%–5%), and loss claim triggers | `{"species": "Paddy", "acres": 3.0}` |
| `POST` | `/api/estimate-yield/` | Machine learning crop yield prediction in Quintals/Tons across 3 scenarios | `{"species": "Ragi", "rainfall": 850, "soil_ph": 6.5, "elevation": 800}` |
| `POST` | `/api/diagnostics/` | Satellite drought scan, 9-month NDVI trend, SPI index, & nearest water reservoir | `{"latitude": 17.3297, "longitude": 76.8343}` |
| `POST` | `/api/drought-scan/` | Scans all 26 Karnataka district monitoring stations for systemic drought stress | `{}` |
| `POST` | `/api/fire-risk/` | Canadian FWI score, Rothermel-Huygens 24h spread ellipse, & KFD dispatch | `{"latitude": 11.6664, "longitude": 76.6293}` |
| `POST` | `/api/fire-scan/` | Scans 20 Karnataka forest reserves for real-time fire weather susceptibility | `{}` |
| `GET`  | `/api/thermal-hotspots/`| NASA FIRMS & ISRO Bhuvan live active satellite infrared hotspots feed | `{}` |
| `GET`  | `/api/forest-boundaries/`| GeoJSON polygons for all 20 protected forest and tiger reserves in Karnataka | `{}` |
| `POST` | `/api/pest-disease/` | 42-disease live weather vulnerability scan & nearest agro-input stores | `{"latitude": 14.7946, "longitude": 75.4011}` |
| `GET`  | `/api/live-alerts/` | Live multi-hub agricultural weather alerts across Karnataka | `{}` |

---

## 🛠️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Backend Framework** | Python 3.11, Django 5.x, Django REST Framework (DRF) |
| **AI & Conversational LLM** | Google Gemini 1.5 Flash (Google AI Studio Free Tier) + UAS Karnataka Agronomy Engine |
| **Frontend & UI** | Vanilla JS (ES6+), Glassmorphism Design System v3, CSS3 Custom Properties, Plus Jakarta Sans |
| **GIS & Mapping** | Leaflet.js 1.9.4, Turf.js, Leaflet Draw, GeoJSON Karnataka Layers |
| **Data Visualizations** | Chart.js 4.4 |
| **Live Telemetry Feeds** | Open-Meteo Weather API, ISRIC SoilGrids, CGWB Aquifers, NASA FIRMS Thermal Hotspots |
| **Voice & Accessibility** | HTML5 Web Speech API (`SpeechRecognition` & `SpeechSynthesisUtterance` for `kn-IN` & `en-IN`) |
| **Deployment & WSGI** | Gunicorn 21.x, WhiteNoise 6.6, Render Web Service |

---

## ⚡ Quickstart & Local Installation

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
# Windows:
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Initialize Database & Seed Botanical Profiles
```bash
cd terraguard
python manage.py migrate
python manage.py seed_data
```

### 4. Run Development Server
```bash
python manage.py runserver
```

Open your browser at **`http://127.0.0.1:8000/`**.

---

## 🌐 Full Bilingual & Voice Support (ಕನ್ನಡ & English)

TerraGuard features zero-latency dynamic translation between **English** and **Kannada (ಕನ್ನಡ)** covering all technical metrics, botanical profiles, agroforestry explanations, biological mechanisms, fertilizer split schedules, and government schemes, complete with **natural voice speech synthesis** for rural accessibility.

---

## 📄 License & Dedication

This project is developed as an open-source initiative for climate-smart agriculture, farmer prosperity, and environmental conservation in Karnataka.

---

**Built with ❤️ for Karnataka Farmers & Forest Protectors by Rohan**
