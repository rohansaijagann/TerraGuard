"""
20-Year Agroforestry Carbon Credit Monetization Engine (Verra / Gold Standard / REDD+).
Simulates annual and cumulative biomass accumulation and carbon dioxide equivalent
sequestration (tCO2e / acre / year) across 20-year tree growth horizons in Karnataka:
- Verra VM0042 & Gold Standard verified carbon offset methodologies
- Calculates Voluntary Carbon Market (VCM) revenues at $15 / tCO2e (₹1,250 per credit)
- Multi-tier agroforestry tree growth curves and farmer carbon payout schedule
"""

# Species-Specific Carbon Sequestration Growth Curves (tCO2e / acre / year by growth stage)
TREE_CARBON_SEQUESTRATION_MODELS = {
    "melia dubia": {"yr1_3": 6.5, "yr4_7": 14.2, "yr8_12": 11.0, "yr13_20": 6.0, "harvest_cycle_yrs": 6, "wood_density": 0.52},
    "malabar neem": {"yr1_3": 6.5, "yr4_7": 14.2, "yr8_12": 11.0, "yr13_20": 6.0, "harvest_cycle_yrs": 6, "wood_density": 0.52},
    "bamboo": {"yr1_3": 9.0, "yr4_7": 18.5, "yr8_12": 16.0, "yr13_20": 15.0, "harvest_cycle_yrs": 4, "wood_density": 0.70},
    "teak": {"yr1_3": 3.8, "yr4_7": 8.5, "yr8_12": 12.8, "yr13_20": 10.5, "harvest_cycle_yrs": 20, "wood_density": 0.65},
    "sandalwood": {"yr1_3": 2.5, "yr4_7": 5.2, "yr8_12": 8.0, "yr13_20": 9.5, "harvest_cycle_yrs": 18, "wood_density": 0.90},
    "pongamia": {"yr1_3": 4.5, "yr4_7": 9.0, "yr8_12": 11.5, "yr13_20": 10.0, "harvest_cycle_yrs": 25, "wood_density": 0.68},
    "honge": {"yr1_3": 4.5, "yr4_7": 9.0, "yr8_12": 11.5, "yr13_20": 10.0, "harvest_cycle_yrs": 25, "wood_density": 0.68},
    "silver oak": {"yr1_3": 4.0, "yr4_7": 9.5, "yr8_12": 11.0, "yr13_20": 8.0, "harvest_cycle_yrs": 15, "wood_density": 0.55},
    "rosewood": {"yr1_3": 2.2, "yr4_7": 5.0, "yr8_12": 7.8, "yr13_20": 9.0, "harvest_cycle_yrs": 30, "wood_density": 0.85},
    "eucalyptus": {"yr1_3": 7.0, "yr4_7": 15.0, "yr8_12": 12.0, "yr13_20": 7.0, "harvest_cycle_yrs": 5, "wood_density": 0.72},
    "casuarina": {"yr1_3": 6.8, "yr4_7": 13.5, "yr8_12": 10.5, "yr13_20": 6.5, "harvest_cycle_yrs": 5, "wood_density": 0.80},
    "moringa": {"yr1_3": 5.0, "yr4_7": 7.5, "yr8_12": 6.0, "yr13_20": 5.0, "harvest_cycle_yrs": 10, "wood_density": 0.45},
    "jackfruit": {"yr1_3": 3.5, "yr4_7": 7.0, "yr8_12": 9.2, "yr13_20": 9.8, "harvest_cycle_yrs": 25, "wood_density": 0.60},
    "mango": {"yr1_3": 3.0, "yr4_7": 6.5, "yr8_12": 8.5, "yr13_20": 9.0, "harvest_cycle_yrs": 30, "wood_density": 0.58}
}

def calculate_20yr_carbon_credits(species_name, acres=1.0, price_per_credit_usd=15.0, usd_to_inr=83.5):
    """
    Computes year-by-year 20-year carbon sequestration trajectory and monetization cashflow.
    """
    s_clean = species_name.lower()
    matched = None
    for k in TREE_CARBON_SEQUESTRATION_MODELS:
        if k in s_clean:
            matched = TREE_CARBON_SEQUESTRATION_MODELS[k]
            break

    if not matched:
        is_tree = "tree" in s_clean or "timber" in s_clean
        base_rate = 5.5 if is_tree else 1.8
        matched = {"yr1_3": base_rate * 0.6, "yr4_7": base_rate * 1.3, "yr8_12": base_rate * 1.1, "yr13_20": base_rate * 0.9, "harvest_cycle_yrs": 10, "wood_density": 0.60}

    price_inr_per_credit = price_per_credit_usd * usd_to_inr # ~ ₹1,252 per credit

    yearly_trajectory = []
    cumulative_co2 = 0.0
    cumulative_rev_inr = 0

    for yr in range(1, 21):
        if yr <= 3:
            annual_rate = matched["yr1_3"]
        elif yr <= 7:
            annual_rate = matched["yr4_7"]
        elif yr <= 12:
            annual_rate = matched["yr8_12"]
        else:
            annual_rate = matched["yr13_20"]

        annual_co2_acre = round(annual_rate * acres, 2)
        annual_rev_inr = round(annual_co2_acre * price_inr_per_credit)
        
        cumulative_co2 = round(cumulative_co2 + annual_co2_acre, 2)
        cumulative_rev_inr = round(cumulative_rev_inr + annual_rev_inr)

        yearly_trajectory.append({
            "year": yr,
            "annual_tco2e": annual_co2_acre,
            "annual_payout_inr": annual_rev_inr,
            "cumulative_tco2e": cumulative_co2,
            "cumulative_payout_inr": cumulative_rev_inr
        })

    # Milestone snapshots (Year 1, Year 5, Year 10, Year 20)
    y1 = yearly_trajectory[0]
    y5 = yearly_trajectory[4]
    y10 = yearly_trajectory[9]
    y20 = yearly_trajectory[19]

    return {
        "species": species_name,
        "acres": round(acres, 1),
        "vcm_credit_price": f"${price_per_credit_usd} (₹{round(price_inr_per_credit)}) / tCO₂e",
        "standard": "Verra VM0042 / Gold Standard Agri-Carbon Code",
        "milestones": {
            "year_1": {"co2_sequestered": f"{y1['cumulative_tco2e']} tCO₂e", "cumulative_revenue": f"₹{y1['cumulative_payout_inr']:,}"},
            "year_5": {"co2_sequestered": f"{y5['cumulative_tco2e']} tCO₂e", "cumulative_revenue": f"₹{y5['cumulative_payout_inr']:,}"},
            "year_10": {"co2_sequestered": f"{y10['cumulative_tco2e']} tCO₂e", "cumulative_revenue": f"₹{y10['cumulative_payout_inr']:,}"},
            "year_20": {"co2_sequestered": f"{y20['cumulative_tco2e']} tCO₂e", "cumulative_revenue": f"₹{y20['cumulative_payout_inr']:,}"}
        },
        "total_20yr_sequestration": f"{y20['cumulative_tco2e']} tCO₂e",
        "total_20yr_carbon_wealth": f"₹{y20['cumulative_payout_inr']:,}",
        "yearly_trajectory": yearly_trajectory
    }
