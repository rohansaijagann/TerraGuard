"""
Precision Fertilizer & NPK Stoichiometric Nutrient Calculator.
Computes site-specific nutrient balance (N, P2O5, K2O in kg/acre) based on:
- Target crop botanical nutrient extraction index
- Live soil available Nitrogen (cg/kg), Soil pH, and Soil Organic Carbon (SOC)
- Recommends commercial bags: Urea (46% N), DAP (18-46-0), MOP (60% K2O)
- 3-Stage Split application timeline (Basal, Vegetative, Flowering)
- Organic alternative package (FYM Compost, Vermicompost, Neem Cake)
"""

CROP_NPK_REQUIREMENTS = {
    # ── Cereals & Millets (N-P-K in kg / acre) ──
    "ragi": {"n": 40, "p": 20, "k": 20, "fym_tons": 3.0, "organic_support": "Neem cake 100kg + Azospirillum"},
    "finger millet": {"n": 40, "p": 20, "k": 20, "fym_tons": 3.0, "organic_support": "Neem cake 100kg + Azospirillum"},
    "jowar": {"n": 32, "p": 16, "k": 16, "fym_tons": 2.5, "organic_support": "FYM 2.5 tons + PSB biofertilizer"},
    "sorghum": {"n": 32, "p": 16, "k": 16, "fym_tons": 2.5, "organic_support": "FYM 2.5 tons + PSB biofertilizer"},
    "bajra": {"n": 28, "p": 14, "k": 14, "fym_tons": 2.0, "organic_support": "Compost 2 tons + Azotobacter"},
    "pearl millet": {"n": 28, "p": 14, "k": 14, "fym_tons": 2.0, "organic_support": "Compost 2 tons + Azotobacter"},
    "paddy": {"n": 48, "p": 24, "k": 24, "fym_tons": 4.0, "organic_support": "Green manure (Dhaincha/Sunnhemp) + Blue Green Algae"},
    "rice": {"n": 48, "p": 24, "k": 24, "fym_tons": 4.0, "organic_support": "Green manure (Dhaincha/Sunnhemp) + Blue Green Algae"},
    "maize": {"n": 60, "p": 30, "k": 24, "fym_tons": 4.0, "organic_support": "Enriched FYM + Zinc Sulphate 10kg/acre"},
    "wheat": {"n": 40, "p": 20, "k": 16, "fym_tons": 3.0, "organic_support": "Vermicompost 1 ton + Trichoderma"},

    # ── Pulses & Oilseeds ──
    "toor dal": {"n": 10, "p": 20, "k": 10, "fym_tons": 2.0, "organic_support": "Rhizobium seed treatment + PSB (N-fixing legume)"},
    "pigeon pea": {"n": 10, "p": 20, "k": 10, "fym_tons": 2.0, "organic_support": "Rhizobium seed treatment + PSB (N-fixing legume)"},
    "chickpea": {"n": 10, "p": 20, "k": 10, "fym_tons": 2.0, "organic_support": "Rhizobium leguminosarum + Sulphur 10kg/acre"},
    "groundnut": {"n": 10, "p": 20, "k": 18, "fym_tons": 3.0, "organic_support": "Gypsum 200kg/acre (for pod filling) + Rhizobium"},
    "sunflower": {"n": 24, "p": 36, "k": 24, "fym_tons": 3.0, "organic_support": "Borax 2kg/acre foliar spray for seed setting"},
    "cotton": {"n": 48, "p": 24, "k": 24, "fym_tons": 4.0, "organic_support": "Neem cake 150kg + Magnesium Sulphate 10kg"},
    "soybean": {"n": 12, "p": 24, "k": 16, "fym_tons": 2.5, "organic_support": "Bradyrhizobium japonicum + PSB"},
    "safflower": {"n": 16, "p": 16, "k": 10, "fym_tons": 2.0, "organic_support": "FYM 2 tons + VAM fungal inoculation"},

    # ── Commercial Cash Crops & Spices ──
    "coffee (arabica)": {"n": 64, "p": 48, "k": 64, "fym_tons": 5.0, "organic_support": "Shade tree leaf litter compost + Bone meal"},
    "coffee (robusta)": {"n": 56, "p": 40, "k": 56, "fym_tons": 5.0, "organic_support": "Composted coffee pulp + Rock phosphate"},
    "black pepper": {"n": 40, "p": 16, "k": 56, "fym_tons": 4.0, "organic_support": "Trichoderma harzianum + Neem cake 1kg/vine"},
    "cardamom": {"n": 30, "p": 30, "k": 60, "fym_tons": 4.0, "organic_support": "Forest mulch + Dolomite 200g/clump for pH balance"},
    "arecanut": {"n": 40, "p": 16, "k": 56, "fym_tons": 5.0, "organic_support": "Areca leaf compost + Green manuring with Cowpea"},
    "coconut": {"n": 50, "p": 32, "k": 120, "fym_tons": 6.0, "organic_support": "Coir pith compost + Common salt (NaCl) 1kg/palm"},
    "chilli": {"n": 40, "p": 20, "k": 20, "fym_tons": 4.0, "organic_support": "Panchagavya foliar spray 3% + Neem cake"},
    "turmeric": {"n": 48, "p": 24, "k": 36, "fym_tons": 6.0, "organic_support": "Heavy mulching with green leaves (10 tons) + FYM"},
    "ginger": {"n": 48, "p": 24, "k": 36, "fym_tons": 6.0, "organic_support": "Trichoderma enriched FYM + Bio-NPK consortium"},
    "sugarcane": {"n": 100, "p": 40, "k": 50, "fym_tons": 8.0, "organic_support": "Press mud 4 tons + Acetobacter diazotrophicus"},

    # ── Horticulture & Fruit Trees ──
    "pomegranate": {"n": 36, "p": 24, "k": 36, "fym_tons": 5.0, "organic_support": "Micronutrient drip mixture (Fe, Zn, B) + PSB"},
    "mango": {"n": 40, "p": 20, "k": 40, "fym_tons": 6.0, "organic_support": "Paclobutrazol regulated canopy nutrition + FYM"},
    "banana": {"n": 80, "p": 24, "k": 96, "fym_tons": 6.0, "organic_support": "Drip fertigation + Pseudostem compost"},
    "guava": {"n": 30, "p": 15, "k": 30, "fym_tons": 4.0, "organic_support": "Vermicompost 10kg/tree + Zinc Sulphate"},
    "fig": {"n": 24, "p": 16, "k": 24, "fym_tons": 3.5, "organic_support": "Neem cake 2kg/plant + Drip fertigation"},

    # ── High-Value Timber & Agroforestry Trees (Annual Maintenance / Tree) ──
    "melia dubia": {"n": 20, "p": 10, "k": 15, "fym_tons": 2.0, "organic_support": "Year 1-3 ring placement FYM 10kg/tree"},
    "malabar neem": {"n": 20, "p": 10, "k": 15, "fym_tons": 2.0, "organic_support": "Year 1-3 ring placement FYM 10kg/tree"},
    "bamboo": {"n": 30, "p": 15, "k": 20, "fym_tons": 3.0, "organic_support": "Clump trench composting with leaf mulch"},
    "teak": {"n": 15, "p": 8, "k": 12, "fym_tons": 2.0, "organic_support": "Deep pit FYM 5kg + VAM mycorrhiza at planting"},
    "sandalwood": {"n": 10, "p": 6, "k": 10, "fym_tons": 1.5, "organic_support": "Secondary host leguminous pruning mulch (Cajanus cajan)"},
    "silver oak": {"n": 15, "p": 8, "k": 12, "fym_tons": 2.0, "organic_support": "Leaf litter natural decomposition"},
    "moringa": {"n": 25, "p": 15, "k": 20, "fym_tons": 3.0, "organic_support": "Vermicompost 5kg/tree + Wood ash for Potassium"}
}

def calculate_precision_fertilizer_dosage(species_name, soil_ph=6.5, soil_nitrogen=180, soil_soc=0.6, acres=1.0):
    """
    Computes exact stoichiometric NPK recommendations, commercial bags, split schedule, and costs.
    """
    s_clean = species_name.lower()
    matched_req = None
    for k in CROP_NPK_REQUIREMENTS:
        if k in s_clean:
            matched_req = CROP_NPK_REQUIREMENTS[k]
            break

    # Fallback generic requirement if not in explicit dictionary
    if not matched_req:
        is_tree = "tree" in s_clean or "timber" in s_clean
        matched_req = {"n": 20 if is_tree else 35, "p": 10 if is_tree else 18, "k": 15 if is_tree else 20, "fym_tons": 2.5, "organic_support": "FYM Compost + Bio-NPK"}

    base_n = matched_req["n"]
    base_p = matched_req["p"]
    base_k = matched_req["k"]

    # 1. Soil-Test Nutrient Adjustments
    # Nitrogen Adjustment (Soil test baseline: 180 cg/kg)
    n_soil_ratio = max(0.6, min(1.4, 180.0 / max(60, soil_nitrogen)))
    adj_n = base_n * n_soil_ratio

    # Phosphorus Fixation Adjustment based on soil pH (P binds to Al/Fe at pH < 5.8 and Ca at pH > 7.8)
    p_efficiency = 1.0
    if soil_ph < 5.8:
        p_efficiency = 1.25 # Acidic fixation: requires 25% higher dose or lime correction
    elif soil_ph > 7.8:
        p_efficiency = 1.20 # Calcareous fixation: requires gypsum/sulphur conditioning
    adj_p = base_p * p_efficiency

    # Potassium adjustment based on Organic Carbon (SOC)
    k_efficiency = max(0.8, min(1.2, 1.0 - (soil_soc - 0.5) * 0.3))
    adj_k = base_k * k_efficiency

    # 2. Commercial Fertilizer Bag Conversion
    # DAP (18% N, 46% P2O5) -> Supplies all P and part of N
    dap_kg = round((adj_p / 0.46), 1)
    n_from_dap = dap_kg * 0.18

    # Remaining N supplied via Urea (46% N)
    remaining_n = max(0.0, adj_n - n_from_dap)
    urea_kg = round((remaining_n / 0.46), 1)

    # MOP / Muriate of Potash (60% K2O)
    mop_kg = round((adj_k / 0.60), 1)

    # 3. Total Commercial Bags (Urea 45kg bag, DAP 50kg bag, MOP 50kg bag)
    urea_bags = round((urea_kg * acres) / 45.0, 1)
    dap_bags = round((dap_kg * acres) / 50.0, 1)
    mop_bags = round((mop_kg * acres) / 50.0, 1)

    # 4. Government Subsidized Price Estimates (Karnataka DBT rates)
    # Urea ~ ₹268/45kg, DAP ~ ₹1350/50kg, MOP ~ ₹1700/50kg
    cost_urea = round((urea_kg * acres / 45.0) * 268)
    cost_dap = round((dap_kg * acres / 50.0) * 1350)
    cost_mop = round((mop_kg * acres / 50.0) * 1700)
    total_fertilizer_cost = cost_urea + cost_dap + cost_mop

    # 5. Split Application Schedule (Basal, Vegetative, Flowering)
    split_schedule = [
        {
            "stage": "Basal Dressing (At Sowing / Planting)",
            "stage_kn": "ಬುಡ ಗೊಬ್ಬರ (ಬಿತ್ತನೆ / ನಾಟಿ ಸಮಯದಲ್ಲಿ)",
            "urea_kg": round(urea_kg * 0.40 * acres, 1),
            "dap_kg": round(dap_kg * 1.00 * acres, 1),
            "mop_kg": round(mop_kg * 0.50 * acres, 1),
            "instructions": "Incorporate entire DAP + 50% MOP + 40% Urea into seed furrows with FYM compost.",
            "instructions_kn": "ಸಂಪೂರ್ಣ ಡಿಎಪಿ + ೫೦% ಪೊಟ್ಯಾಶ್ + ೪೦% ಯೂರಿಯಾವನ್ನು ಕಾಂಪೋಸ್ಟ್ ಜೊತೆ ಸಾಲಿನಲ್ಲಿ ಹಾಕಿ."
        },
        {
            "stage": "Top Dressing Stage 1 (Day 25–35 Vegetative)",
            "stage_kn": "ಮೇಲುಗೊಬ್ಬರ ಹಂತ ೧ (೨೫-೩೫ ನೇ ದಿನ ಬೆಳವಣಿಗೆ ಹಂತ)",
            "urea_kg": round(urea_kg * 0.35 * acres, 1),
            "dap_kg": 0.0,
            "mop_kg": 0.0,
            "instructions": "Side-dress with Urea after first weeding; irrigate immediately.",
            "instructions_kn": "ಕಳೆ ತೆಗೆದ ನಂತರ ಯೂರಿಯಾ ಉದುರಿಸಿ, ತಕ್ಷಣ ನೀರು ಹಾಯಿಸಿ."
        },
        {
            "stage": "Top Dressing Stage 2 (Day 50–65 Flowering / Pod Formation)",
            "stage_kn": "ಮೇಲುಗೊಬ್ಬರ ಹಂತ ೨ (೫೦-೬೫ ನೇ ದಿನ ಹೂವಾಡುವ ಹಂತ)",
            "urea_kg": round(urea_kg * 0.25 * acres, 1),
            "dap_kg": 0.0,
            "mop_kg": round(mop_kg * 0.50 * acres, 1),
            "instructions": "Apply remaining Urea + MOP for superior grain/fruit filling.",
            "instructions_kn": "ಉಳಿದ ಯೂರಿಯಾ ಮತ್ತು ಪೊಟ್ಯಾಶ್ ಹಾಕಿ ಉತ್ತಮ ಕಾಳು/ಹಣ್ಣು ತುಂಬಲು ನೆರವಾಗಿ."
        }
    ]

    return {
        "species": species_name,
        "acres": round(acres, 1),
        "nutrient_recommendation_kg_acre": {
            "nitrogen_n": round(adj_n, 1),
            "phosphorus_p2o5": round(adj_p, 1),
            "potassium_k2o": round(adj_k, 1)
        },
        "commercial_fertilizers": {
            "urea": {"kg_per_acre": urea_kg, "total_kg": round(urea_kg * acres, 1), "bags_45kg": urea_bags, "subsidized_cost": cost_urea},
            "dap": {"kg_per_acre": dap_kg, "total_kg": round(dap_kg * acres, 1), "bags_50kg": dap_bags, "subsidized_cost": cost_dap},
            "mop": {"kg_per_acre": mop_kg, "total_kg": round(mop_kg * acres, 1), "bags_50kg": mop_bags, "subsidized_cost": cost_mop}
        },
        "total_fertilizer_budget": f"₹{new_format_inr(total_fertilizer_cost)}",
        "split_schedule": split_schedule,
        "organic_package": {
            "fym_compost_tons": round(matched_req["fym_tons"] * acres, 1),
            "biofertilizer_support": matched_req["organic_support"]
        }
    }

def new_format_inr(val):
    s = str(int(val))
    if len(s) <= 3:
        return s
    first = s[-3:]
    rest = s[:-3]
    parts = []
    while len(rest) > 2:
        parts.insert(0, rest[-2:])
        rest = rest[:-2]
    if rest:
        parts.insert(0, rest)
    return ",".join(parts) + "," + first
