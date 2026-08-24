"""
Pradhan Mantri Fasal Bima Yojana (PMFBY) Karnataka Crop Insurance & Risk Coverage Calculator.
Computes site-specific crop insurance parameters, subsidized farmer premium share,
scale of finance (Sum Insured per acre), and automated claim trigger conditions:
- 1.5% Premium for Rabi crops (Wheat, Bengal Gram, Safflower)
- 2.0% Premium for Kharif crops (Paddy, Ragi, Jowar, Maize, Groundnut, Toor Dal)
- 5.0% Premium for Commercial & Horticultural crops (Cotton, Pomegranate, Banana, Chilli, Turmeric)
- Automatic Loss Indemnity Triggers under Samrakshane Karnataka Portal
"""

# Scale of Finance (Sum Insured per Acre in ₹) and Category Classification under PMFBY Karnataka
PMFBY_CROP_SCALES = {
    # ── Kharif Crops (2.0% Farmer Premium) ──
    "ragi": {"sum_insured_acre": 22000, "season": "Kharif", "farmer_premium_pct": 2.0, "category": "Food Grain / Millet"},
    "finger millet": {"sum_insured_acre": 22000, "season": "Kharif", "farmer_premium_pct": 2.0, "category": "Food Grain / Millet"},
    "paddy": {"sum_insured_acre": 34000, "season": "Kharif / Rabi", "farmer_premium_pct": 2.0, "category": "Cereal Food Grain"},
    "rice": {"sum_insured_acre": 34000, "season": "Kharif / Rabi", "farmer_premium_pct": 2.0, "category": "Cereal Food Grain"},
    "jowar": {"sum_insured_acre": 19000, "season": "Kharif / Rabi", "farmer_premium_pct": 2.0, "category": "Dryland Cereal"},
    "sorghum": {"sum_insured_acre": 19000, "season": "Kharif / Rabi", "farmer_premium_pct": 2.0, "category": "Dryland Cereal"},
    "bajra": {"sum_insured_acre": 16500, "season": "Kharif", "farmer_premium_pct": 2.0, "category": "Millet"},
    "pearl millet": {"sum_insured_acre": 16500, "season": "Kharif", "farmer_premium_pct": 2.0, "category": "Millet"},
    "maize": {"sum_insured_acre": 26000, "season": "Kharif / Rabi", "farmer_premium_pct": 2.0, "category": "Coarse Cereal"},
    "toor dal": {"sum_insured_acre": 25000, "season": "Kharif", "farmer_premium_pct": 2.0, "category": "Pulse"},
    "pigeon pea": {"sum_insured_acre": 25000, "season": "Kharif", "farmer_premium_pct": 2.0, "category": "Pulse"},
    "groundnut": {"sum_insured_acre": 28000, "season": "Kharif", "farmer_premium_pct": 2.0, "category": "Oilseed"},
    "soybean": {"sum_insured_acre": 24000, "season": "Kharif", "farmer_premium_pct": 2.0, "category": "Oilseed"},

    # ── Rabi Crops (1.5% Farmer Premium) ──
    "wheat": {"sum_insured_acre": 21000, "season": "Rabi", "farmer_premium_pct": 1.5, "category": "Rabi Cereal"},
    "chickpea": {"sum_insured_acre": 22500, "season": "Rabi", "farmer_premium_pct": 1.5, "category": "Rabi Pulse"},
    "safflower": {"sum_insured_acre": 17000, "season": "Rabi", "farmer_premium_pct": 1.5, "category": "Rabi Oilseed"},
    "sunflower": {"sum_insured_acre": 20000, "season": "Kharif / Rabi", "farmer_premium_pct": 1.5, "category": "Oilseed"},

    # ── Commercial & Horticultural Crops (5.0% Farmer Premium) ──
    "cotton": {"sum_insured_acre": 38000, "season": "Commercial", "farmer_premium_pct": 5.0, "category": "Commercial Fiber"},
    "chilli": {"sum_insured_acre": 45000, "season": "Horticultural", "farmer_premium_pct": 5.0, "category": "Commercial Spice"},
    "pomegranate": {"sum_insured_acre": 85000, "season": "Horticultural", "farmer_premium_pct": 5.0, "category": "Perennial Fruit"},
    "banana": {"sum_insured_acre": 55000, "season": "Horticultural", "farmer_premium_pct": 5.0, "category": "Horticulture"},
    "mango": {"sum_insured_acre": 48000, "season": "Horticultural", "farmer_premium_pct": 5.0, "category": "Orchard Fruit"},
    "turmeric": {"sum_insured_acre": 50000, "season": "Horticultural", "farmer_premium_pct": 5.0, "category": "Commercial Spice"},
    "ginger": {"sum_insured_acre": 60000, "season": "Horticultural", "farmer_premium_pct": 5.0, "category": "High Value Spice"},
    "arecanut": {"sum_insured_acre": 75000, "season": "Plantation", "farmer_premium_pct": 5.0, "category": "Plantation Crop"},
    "coffee": {"sum_insured_acre": 65000, "season": "Plantation", "farmer_premium_pct": 5.0, "category": "Plantation Crop"},
    "black pepper": {"sum_insured_acre": 42000, "season": "Plantation", "farmer_premium_pct": 5.0, "category": "Spices Intercrop"},
    "cardamom": {"sum_insured_acre": 70000, "season": "Plantation", "farmer_premium_pct": 5.0, "category": "High Value Spice"},
    "sugarcane": {"sum_insured_acre": 65000, "season": "Commercial", "farmer_premium_pct": 5.0, "category": "Commercial Cash Crop"}
}

def calculate_pmfby_crop_insurance(species_name, acres=1.0):
    """
    Calculates PMFBY sum insured, farmer payable premium share, and government subsidy support.
    """
    s_clean = species_name.lower()
    matched = None
    for k in PMFBY_CROP_SCALES:
        if k in s_clean:
            matched = PMFBY_CROP_SCALES[k]
            break

    if not matched:
        is_tree = "tree" in s_clean or "timber" in s_clean
        matched = {"sum_insured_acre": 35000 if is_tree else 25000, "season": "Kharif / Commercial", "farmer_premium_pct": 5.0 if is_tree else 2.0, "category": "Agroforestry / Field Crop"}

    sum_insured_acre = matched["sum_insured_acre"]
    total_sum_insured = round(sum_insured_acre * acres)
    premium_pct = matched["farmer_premium_pct"]
    
    # Farmer Subsidized Premium (1.5% to 5.0%)
    farmer_payable_premium = round((total_sum_insured * premium_pct) / 100.0)

    # Actual Actuarial Premium is typically ~12-16% in Karnataka; State + Central Govt pay the remaining 85%+!
    actuarial_rate = 14.5
    total_actuarial_premium = round((total_sum_insured * actuarial_rate) / 100.0)
    govt_subsidy_share = total_actuarial_premium - farmer_payable_premium

    claim_triggers = [
        {"trigger": "Prevented Sowing / Planting Risk", "condition": "Monsoon rainfall deficit > 75% up to July 15th preventing normal sowing (Up to 25% sum insured immediate payout)."},
        {"trigger": "Mid-Season Adversity (Drought / Flood)", "condition": "Consecutive dry spells > 21 days during flowering stage causing >50% expected yield loss."},
        {"trigger": "Post-Harvest Localized Calamities", "condition": "Unseasonal cyclone / hailstorm damage to harvested crops kept in open field for drying within 14 days of cut."},
        {"trigger": "End-of-Season Crop Cutting Experiment (CCE)", "condition": "Actual Gram Panchayat average yield falling below historical threshold yield."}
    ]

    return {
        "species": species_name,
        "acres": round(acres, 1),
        "season": matched["season"],
        "category": matched["category"],
        "sum_insured_per_acre": f"₹{sum_insured_acre:,}",
        "total_sum_insured": f"₹{total_sum_insured:,}",
        "farmer_premium_rate": f"{premium_pct}%",
        "farmer_payable_premium": f"₹{farmer_payable_premium:,}",
        "govt_subsidy_absorbed": f"₹{govt_subsidy_share:,} ({(100 - round((farmer_payable_premium/max(1,total_actuarial_premium))*100))}% Govt Subsidized)",
        "claim_triggers": claim_triggers,
        "portal_name": "Samrakshane Portal (Karnataka Govt)",
        "portal_url": "https://samrakshane.karnataka.gov.in"
    }
