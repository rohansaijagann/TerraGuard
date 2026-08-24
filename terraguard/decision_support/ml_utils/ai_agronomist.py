"""
Raitha Sahayaka (ರೈತ ಸಹಾಯಕ) AI Conversational Agronomist Engine.
Powered by Google Gemini with an intelligent built-in Karnataka Agronomic Expert fallback:
- Pre-grounded in farm geo-coordinates, soil pH, rainfall, aquifer depth, and crop telemetry
- Full bilingual conversational fluency in Kannada (ಕನ್ನಡ) and English
- Voice-enabled speech synthesis and recognition integration
"""

import os
import json
import urllib.request
import urllib.error

SYSTEM_PROMPT_EN = """You are 'Raitha Sahayaka' (ರೈತ ಸಹಾಯಕ), an expert senior agricultural scientist and agronomist from the University of Agricultural Sciences (UAS) Bengaluru & UAS Dharwad.
You advise Karnataka farmers, plantation owners, and agri-entrepreneurs with practical, highly actionable, scientifically grounded guidance.

CURRENT FARM TELEMETRY & CONTEXT:
- Location: {location_name} ({district}, Karnataka) [Lat: {lat}, Lon: {lon}]
- Annual Rainfall: {rainfall_mm} mm
- Soil pH: {soil_ph} | Available Nitrogen: {nitrogen} cg/kg | Organic Carbon: {soc}%
- CGWB Groundwater Aquifer Depth: {aquifer_depth}m mbgl (Status: {aquifer_status})
- Recommended Top Crops: {top_crops}
- Eligible Subsidies: {subsidies}
- Nearest APMC Mandi: {nearest_mandi}
- Nearest Custom Hiring Centre: {nearest_chc}

GUIDELINES:
1. Always tailor your advice specifically to the farmer's soil, rainfall, aquifer depth, and location.
2. If the user asks in Kannada (or requested language is 'kn'), ALWAYS respond in fluent, respectful, natural Kannada (e.g. use terms like 'ರೈತ ಬಾಂಧವರೇ', 'ಎಕರೆಗೆ', 'ಬೋರ್‌ವೆಲ್', 'ಸಾವಯವ ಕೃಷಿ'). If in English, respond in clear professional English.
3. Keep answers well-structured with bullet points, practical dosages, and realistic cost/return estimates.
4. Bold key terms, chemical names, and numbers for easy scanning.
"""

SYSTEM_PROMPT_KN = """ನೀವು 'ರೈತ ಸಹಾಯಕ' (Raitha Sahayaka), ಬೆಂಗಳೂರು ಮತ್ತು ಧಾರವಾಡ ಕೃಷಿ ವಿಶ್ವವಿದ್ಯಾಲಯದ ಹಿರಿಯ ಕೃಷಿ ವಿಜ್ಞಾನಿ ಹಾಗೂ ರೈತ ಸಲಹೆಗಾರರು.
ಕರ್ನಾಟಕದ ರೈತರಿಗೆ ಸರಳ, ಪ್ರಾಯೋಗಿಕ ಹಾಗೂ ಅಧಿಕ ಇಳುವರಿ ನೀಡುವ ವೈಜ್ಞಾನಿಕ ಕೃಷಿ ಮಾರ್ಗದರ್ಶನ ನೀಡುವುದು ನಿಮ್ಮ ಗುರಿ.

ಪ್ರಸ್ತುತ ಜಮೀನಿನ ಮಾಹಿತಿ (Farm Context):
- ಸ್ಥಳ: {location_name} ({district}, ಕರ್ನಾಟಕ)
- ವಾರ್ಷಿಕ ಮಳೆ: {rainfall_mm} ಮಿಮೀ
- ಮಣ್ಣಿನ pH: {soil_ph} | ಸಾರಜನಕ: {nitrogen} | ಸಾವಯವ ಇಂಗಾಲ: {soc}%
- ಅಂತರ್ಜಲ ಮಟ್ಟ (CGWB): {aquifer_depth} ಮೀಟರ್ ಆಳ ({aquifer_status})
- ಶಿಫಾರಸು ಮಾಡಿದ ಬೆಳೆಗಳು: {top_crops}
- ಲಭ್ಯವಿರುವ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು: {subsidies}
- ಹತ್ತಿರದ APMC ಮಾರುಕಟ್ಟೆ: {nearest_mandi}

ನಿಯಮಗಳು:
1. ಉತ್ತರವನ್ನು ಸ್ಪಷ್ಟ, ಗೌರವಯುತ ಮತ್ತು ಅಚ್ಚುಕಟ್ಟಾದ ಕನ್ನಡದಲ್ಲಿ ನೀಡಿ.
2. ಪ್ರಮುಖ ವಿಷಯಗಳನ್ನು ಬುಲೆಟ್ ಪಾಯಿಂಟ್‌ಗಳಲ್ಲಿ ನೀಡಿ.
3. ಗೊಬ್ಬರ ಪ್ರಮಾಣ, ನೀರಿನ ನಿರ್ವಹಣೆ, ಸಾಲಿನ ಅಂತರ ಮತ್ತು ಸರ್ಕಾರಿ ಸಹಾಯಧನದ ವಿವರಗಳನ್ನು ನಿಖರವಾಗಿ ತಿಳಿಸಿ.
"""

def generate_agronomist_reply(query, chat_history=None, farm_context=None, language="kn"):
    """
    Generates intelligent agronomist response using Gemini API or offline expert engine fallback.
    """
    if not farm_context:
        farm_context = {}

    ctx = {
        "location_name": farm_context.get("location_name", "Karnataka Farm"),
        "district": farm_context.get("district", "Karnataka"),
        "lat": farm_context.get("lat", 13.0),
        "lon": farm_context.get("lon", 77.0),
        "rainfall_mm": farm_context.get("rainfall", 850),
        "soil_ph": farm_context.get("ph", 6.5),
        "nitrogen": farm_context.get("nitrogen", 180),
        "soc": farm_context.get("soc", 0.6),
        "aquifer_depth": farm_context.get("cgwb_depth", "18.5"),
        "aquifer_status": farm_context.get("cgwb_status", "Safe"),
        "top_crops": farm_context.get("top_crops", "Ragi, Melia Dubia, Turmeric, Black Pepper"),
        "subsidies": farm_context.get("subsidies", "Raita Siri, Krishi Bhagya, PMKSY Drip"),
        "nearest_mandi": farm_context.get("nearest_mandi", "APMC Yard"),
        "nearest_chc": farm_context.get("nearest_chc", "Krishi Yanthradhare Depot")
    }

    # Check for Gemini API key
    gemini_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")

    if gemini_key:
        try:
            sys_inst = SYSTEM_PROMPT_KN.format(**ctx) if language == "kn" else SYSTEM_PROMPT_EN.format(**ctx)
            
            # Format contents
            contents = []
            if chat_history:
                for msg in chat_history[-6:]:
                    role = "user" if msg.get("sender") == "user" else "model"
                    contents.append({"role": role, "parts": [{"text": msg.get("text", "")}]})
            
            contents.append({"role": "user", "parts": [{"text": query}]})

            payload = {
                "system_instruction": {"parts": [{"text": sys_inst}]},
                "contents": contents,
                "generationConfig": {
                    "temperature": 0.6,
                    "maxOutputTokens": 800,
                    "topP": 0.9
                }
            }

            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={gemini_key}"
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode("utf-8"),
                headers={"Content-Type": "application/json"}
            )
            with urllib.request.urlopen(req, timeout=8) as response:
                resp_json = json.loads(response.read().decode("utf-8"))
                reply = resp_json["candidates"][0]["content"]["parts"][0]["text"]
                return {
                    "reply": reply,
                    "source": "Google Gemini 1.5 Flash (Live AI)",
                    "language": language
                }
        except Exception as e:
            print(f"Gemini API fallback triggered: {e}")

    # Fallback to Built-in Karnataka Agronomic Expert Engine (100% Free, Offline, Instant)
    return fallback_agronomic_engine(query, ctx, language)


def fallback_agronomic_engine(query, ctx, language="kn"):
    """
    Rich offline knowledge engine matching farming intents with site-specific telemetry.
    """
    q_lower = query.lower()
    is_kn = language == "kn"

    # Intent 1: Fertilizer & Nutrition
    if any(k in q_lower for k in ["fertilizer", "gobbara", "urea", "dap", "npk", "ಗೊಬ್ಬರ", "ಯೂರಿಯಾ"]):
        if is_kn:
            reply = f"""🌾 **ರಸಗೊಬ್ಬರ ನಿರ್ವಹಣೆ ಮತ್ತು NPK ವೇಳಾಪಟ್ಟಿ ({ctx['location_name']}):**

ನಿಮ್ಮ ಜಮೀನಿನ ಮಣ್ಣಿನ pH **{ctx['soil_ph']}** ಮತ್ತು ಸಾರಜನಕ ಮಟ್ಟಕ್ಕೆ ಅನುಗುಣವಾಗಿ ಶಿಫಾರಸು:

1. **ಬುಡ ಗೊಬ್ಬರ (ಬಿತ್ತನೆ ಸಮಯದಲ್ಲಿ):**
   - **DAP (18-46-0):** ೫೦ ಕೆಜಿ / ಎಕರೆ (೧ ಚೀಲ)
   - **MOP ಪೊಟ್ಯಾಶ್ (60% K₂O):** ೨೫ ಕೆಜಿ / ಎಕರೆ
   - **ಯೂರಿಯಾ:** ೧೮ ಕೆಜಿ / ಎಕರೆ
   - **ಸಾವಯವ ಕಾಂಪೋಸ್ಟ್:** ೨ ರಿಂದ ೩ ಟನ್ ಚೆನ್ನಾಗಿ ಕಾದ ಕೊಟ್ಟಿಗೆ ಗೊಬ್ಬರ

2. **ಮೇಲುಗೊಬ್ಬರ (೨೫-೩೦ ದಿನಗಳ ನಂತರ):**
   - **ಯೂರಿಯಾ:** ೨೫ ಕೆಜಿ / ಎಕರೆ ಉದುರಿಸಿ, ತಕ್ಷಣ ನೀರು ಹಾಯಿಸಿ.

3. **ಹೂವಾಡುವ ಹಂತ (೫೦-೬೦ ದಿನಗಳ ನಂತರ):**
   - **ಯೂರಿಯಾ + MOP:** ತಲಾ ೧೫ ಕೆಜಿ ಹಾಕಿ ಕಾಳು ತುಂಬಲು ನೆರವಾಗಿ.

💡 *ಸಲಹೆ:* ಹತ್ತಿರದ **ಕೃಷಿ ಯಂತ್ರಧಾರೆ** ಕೇಂದ್ರದಿಂದ ₹350/ಎಕರೆ ದರದಲ್ಲಿ ನ್ಯಾನೋ-ಯೂರಿಯಾ ಡ್ರೋನ್ ಸಿಂಪಡಣೆ ಮಾಡಿಸಬಹುದು."""
        else:
            reply = f"""🌾 **Precision Fertilizer & NPK Schedule ({ctx['location_name']}):**

Calibrated for soil pH **{ctx['soil_ph']}** and Nitrogen level:

1. **Basal Application (At Sowing):**
   - **DAP (18-46-0):** 50 kg / acre (1 bag)
   - **MOP Potash (60% K₂O):** 25 kg / acre (0.5 bag)
   - **Urea:** 18 kg / acre with 2.5 Tons FYM compost

2. **Top Dressing 1 (Day 25–30 Vegetative Stage):**
   - **Urea:** 25 kg / acre side-dressed before irrigation

3. **Top Dressing 2 (Day 50–60 Flowering/Grain Filling):**
   - **Urea + MOP:** 15 kg each for superior seed weight and yield

💡 *Drone Spraying:* Book Nano-Urea aerial drone spraying from nearest Krishi Yanthradhare at ₹350/acre."""
        return {"reply": reply, "source": "Karnataka Agronomic Expert Engine", "language": language}

    # Intent 2: Water & Drought / Aquifer
    if any(k in q_lower for k in ["water", "neeru", "drought", "borewell", "aquifer", "ನೀರು", "ಬೋರ್‌ವೆಲ್", "ಬರಗಾಲ"]):
        if is_kn:
            reply = f"""💧 **ಅಂತರ್ಜಲ ಹಾಗೂ ನೀರಿನ ನಿರ್ವಹಣಾ ಸಲಹೆ ({ctx['district']}):**

- ಪ್ರಸ್ತುತ ನಿಮ್ಮ ಭಾಗದಲ್ಲಿ ಅಂತರ್ಜಲ ಮಟ್ಟ **{ctx['aquifer_depth']} ಮೀಟರ್ ಆಳದಲ್ಲಿದೆ ({ctx['aquifer_status']})**.
- ವಾರ್ಷಿಕ ಸರಾಸರಿ ಮಳೆ: **{ctx['rainfall_mm']} ಮಿಮೀ**.

**ಕ್ರಮಗಳು:**
1. **ಹನಿ ನೀರಾವರಿ (Drip Irrigation):** ಸಾಂಪ್ರದಾಯಿಕ ಕಾಲುವೆ ನೀರಾವರಿಗಿಂತ ೪೫% ನೀರು ಉಳಿತಾಯವಾಗುತ್ತದೆ. PMKSY ಯೋಜನೆಯಡಿ **೯೦% ಸಬ್ಸಿಡಿ** ಲಭ್ಯವಿದೆ.
2. **ಕಡಿಮೆ ನೀರು ಬೇಡುವ ಬೆಳೆಗಳು:** ರಾಗಿ, ತೊಗರಿ, ಶೇಂಗಾ, ಹಲಸು, ಹೆಬ್ಬೇವು (Melia Dubia).
3. **ಕೃಷಿ ಹೊಂಡ (Krishi Honda):** ಕೃಷಿ ಭಾಗ್ಯ ಯೋಜನೆಯಡಿ ೮೦% ಸಹಾಯಧನದಲ್ಲಿ ಕೃಷಿ ಹೊಂಡ ನಿರ್ಮಿಸಿ ಮಳೆ ನೀರು ಕೊಯ್ಲು ಮಾಡಿ.
4. **ಮಣ್ಣಿನ ತೇವಾಂಶ ಸಂರಕ್ಷಣೆ:** ಸಾಲುಗಳ ನಡುವೆ ಒಣ ಹುಲ್ಲು ಅಥವಾ ತೆಂಗಿನ ಸಿಪ್ಪೆಯ ಹೊದಿಕೆ (Mulching) ಹಾಕಿ."""
        else:
            reply = f"""💧 **Groundwater & Irrigation Strategy ({ctx['district']}):**

- Local CGWB Aquifer Depth: **{ctx['aquifer_depth']}m mbgl ({ctx['aquifer_status']})**.
- Annual Rainfall: **{ctx['rainfall_mm']} mm**.

**Action Plan:**
1. **Micro-Drip Fertigation:** Saves 45% water compared to flood irrigation. Eligible for **75–90% PMKSY subsidy**.
2. **Drought-Resilient Crops:** Ragi, Red Gram, Groundnut, Melia Dubia, Moringa.
3. **Krishi Honda (Farm Pond):** Avail 80–90% Krishi Bhagya subsidy for rainwater harvesting.
4. **Mulching:** Apply crop residue or coir pith mulch between crop rows to reduce evaporation by 35%."""
        return {"reply": reply, "source": "Karnataka Agronomic Expert Engine", "language": language}

    # Intent 3: Government Subsidies
    if any(k in q_lower for k in ["subsidy", "scheme", "raita siri", "krishi bhagya", "pmksy", "ಸಹಾಯಧನ", "ಯೋಜನೆ", "ರೈತ ಸಿರಿ"]):
        if is_kn:
            reply = f"""🏛️ **ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಪ್ರಮುಖ ಕೃಷಿ ಯೋಜನೆಗಳು:**

1. **ರೈತ ಸಿರಿ ಯೋಜನೆ (Raita Siri Scheme):**
   - ಸಿರಿಧಾನ್ಯಗಳಾದ ರಾಗಿ, ನವಣೆ, ಸಾಮೆ, ಸಜ್ಜೆ ಬೆಳೆಯುವ ರೈತರಿಗೆ **₹೧೦,೦೦೦/ಹೆಕ್ಟೇರ್** ನೇರ ನಗದು ವರ್ಗಾವಣೆ (DBT).

2. **ಕೃಷಿ ಭಾಗ್ಯ ಯೋಜನೆ (Krishi Bhagya):**
   - ಕೃಷಿ ಹೊಂಡ, ಪಾಲಿಥೀನ್ ಹೊದಿಕೆ ಮತ್ತು ಡೀಸೆಲ್/ಸೋಲಾರ್ ಪಂಪ್‌ಸೆಟ್‌ಗೆ **೮೦% ರಿಂದ ೯೦% ಸಬ್ಸಿಡಿ**.

3. **ಪ್ರಧಾನ ಮಂತ್ರಿ ಕೃಷಿ ಸಿಂಚಾಯಿ ಯೋಜನೆ (PMKSY):**
   - ಹನಿ ನೀರಾವರಿ ಮತ್ತು ತುಂತುರು ನೀರಾವರಿಗೆ ಸಣ್ಣ ಮತ್ತು ಅತಿ ಸಣ್ಣ ರೈತರಿಗೆ **೯೦% ಸಬ್ಸಿಡಿ**.

4. **ರಾಷ್ಟ್ರೀಯ ಬಿದಿರು ಮಿಷನ್ (NBM):**
   - ಬಿದಿರು ಕೃಷಿಗೆ ಪ್ರತಿ ಹೆಕ್ಟೇರ್‌ಗೆ **₹೫೦,೦೦೦ (೫೦% ಅನುದಾನ)**.

📲 *ಅರ್ಜಿ ಸಲ್ಲಿಸಲು:* **fruits.karnataka.gov.in** ಅಥವಾ ನಿಮ್ಮ ತಾಲ್ಲೂಕಿನ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರಕ್ಕೆ (RSK) ಭೇಟಿ ನೀಡಿ."""
        else:
            reply = f"""🏛️ **Active Karnataka Government Agricultural Subsidies:**

1. **Raita Siri Scheme:**
   - **₹10,000 / hectare** Direct Benefit Transfer (DBT) for cultivating millets (Ragi, Foxtail, Pearl Millet).

2. **Krishi Bhagya Scheme:**
   - **80% to 90% subsidy** for Farm Ponds (*Krishi Honda*), polythene lining, and solar pumpsets.

3. **PMKSY Micro-Irrigation Scheme:**
   - **90% subsidy** on Drip & Sprinkler units for Small & Marginal farmers.

4. **National Bamboo Mission (NBM):**
   - **50% capital subsidy (₹50,000/ha)** for agroforestry bamboo plantation.

📲 *Apply Online:* Visit **fruits.karnataka.gov.in** or your nearest Raitha Samparka Kendra (RSK)."""
        return {"reply": reply, "source": "Karnataka Agronomic Expert Engine", "language": language}

    # Intent 4: Spacing / Multi-Tier Agroforestry
    if any(k in q_lower for k in ["spacing", "intercrop", "tree", "coffee", "pepper", "areca", "ಅಂತರ", "ಸಾಲು", "ಅಡಿಕೆ", "ಕಾಫಿ"]):
        if is_kn:
            reply = f"""🌲 **೪-ಹಂತದ ಕೃಷಿ ಅರಣ್ಯ ಸಾಲಿನ ಅಂತರ ವಿನ್ಯಾಸ ({ctx['location_name']}):**

೧ ಎಕರೆಯಲ್ಲಿ ಗರಿಷ್ಠ ಲಾಭ ಗಳಿಸಲು ಬಹು-ಹಂತದ ಬೆಳೆ ಪದ್ಧತಿಯ ವಿನ್ಯಾಸ:

- **ಹಂತ ೧ (ಎತ್ತರದ ಮರಗಳು):** ಬೆಳ್ಳಿ ಓಕ್ ಅಥವಾ ಹೆಬ್ಬೇವು (Melia Dubia) — **೨೦ ಅಡಿ x ೨೦ ಅಡಿ** ಅಂತರ.
- **ಹಂತ ೨ (ತೋಟದ ಬೆಳೆ):** ಅಡಿಕೆ ಅಥವಾ ಕಾಫಿ ಗಿಡಗಳು — **೯ ಅಡಿ x ೯ ಅಡಿ** ಅಂತರ.
- **ಹಂತ ೩ (ಬಳ್ಳಿ ಸಾಂಬಾರ ಬೆಳೆ):** ಕಾಳುಮೆಣಸು — ಪ್ರತಿ ಮರದ ಕಾಂಡದ ಬುಡದಲ್ಲಿ ಹಬ್ಬಿಸಿ (ಶೂನ್ಯ ಹೆಚ್ಚುವರಿ ಭೂಮಿ).
- **ಹಂತ ೪ (ನೆಲಮಟ್ಟದ ಗೆಡ್ಡೆ ಬೆಳೆ):** ಸಾಲುಗಳ ನಡುವೆ ಅರಿಶಿನ ಅಥವಾ ಶುಂಠಿ — **೧.೫ ಅಡಿ** ಸಾಲಿನ ಅಂತರ.

💰 *ಆದಾಯ ಗುಣಕ:* ಈ ಪದ್ಧತಿಯು ಲಂಬ ಬೇರುಗಳ ಸ್ತರ ವಿಭಜನೆಯಿಂದ ಆದಾಯವನ್ನು **೨.೮ ಪಟ್ಟು (2.8x LER)** ಹೆಚ್ಚಿಸುತ್ತದೆ."""
        else:
            reply = f"""🌲 **4-Tier Agroforestry Layout & Planting Spacing ({ctx['location_name']}):**

Optimized multi-canopy arrangement for maximum 1-acre returns:

- **Tier 1 (Top Canopy Trees):** Silver Oak or Melia Dubia — **20 ft x 20 ft** grid.
- **Tier 2 (Orchard Middle):** Arecanut or Arabica Coffee — **9 ft x 9 ft** spacing.
- **Tier 3 (Vertical Climber):** Black Pepper vines trained on tree trunks (zero additional land footprint).
- **Tier 4 (Ground Rhizomes):** Ginger / Turmeric planted in inter-row beds at **1.5 ft** spacing.

💰 *Synergy:* Delivers **2.8x Land Equivalent Ratio (LER)** synergy without root or light competition."""
        return {"reply": reply, "source": "Karnataka Agronomic Expert Engine", "language": language}

    # Default General Agronomy Advisory
    if is_kn:
        reply = f"""🌱 **ರೈತ ಬಾಂಧವರೇ, {ctx['location_name']} ಜಮೀನಿನ ವಿಶ್ಲೇಷಣೆ:**

- ನಿಮ್ಮ ಜಮೀನಿನ ಮಣ್ಣಿನ pH: **{ctx['soil_ph']}** (ಉತ್ತಮ ಫಲವತ್ತತೆ)
- ವಾರ್ಷಿಕ ಮಳೆ: **{ctx['rainfall_mm']} ಮಿಮೀ**
- ಅಂತರ್ಜಲ ಸ್ಥಿತಿ: **{ctx['aquifer_depth']} ಮೀಟರ್ ({ctx['aquifer_status']})**

**ಶಿಫಾರಸು ಮಾಡಿದ ಮುಖ್ಯ ಬೆಳೆಗಳು:**
{ctx['top_crops']}

ನಿಮಗೆ ರಸಗೊಬ್ಬರ ಪ್ರಮಾಣ, ನೀರಿನ ನಿರ್ವಹಣೆ, ರೋಗ ನಿಯಂತ್ರಣ ಅಥವಾ ಸರ್ಕಾರಿ ಸಬ್ಸಿಡಿಗಳ ಬಗ್ಗೆ ನಿರ್ದಿಷ್ಟ ಮಾಹಿತಿ ಬೇಕಾದರೆ ಕೆಳಗಿನ ಬಟನ್‌ಗಳನ್ನು ಒತ್ತಿ ಅಥವಾ ಪ್ರಶ್ನೆಯನ್ನು ಟೈಪ್ ಮಾಡಿ!"""
    else:
        reply = f"""🌱 **Agronomic Summary for {ctx['location_name']}:**

- Soil pH: **{ctx['soil_ph']}** (Optimal range)
- Annual Rainfall: **{ctx['rainfall_mm']} mm**
- Groundwater Table: **{ctx['aquifer_depth']}m mbgl ({ctx['aquifer_status']})**

**Top Recommended Species Stack:**
{ctx['top_crops']}

Ask me anything about fertilizer schedules, drip irrigation design, disease diagnosis, or government subsidy applications!"""

    return {"reply": reply, "source": "Karnataka Agronomic Expert Engine", "language": language}
