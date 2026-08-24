"""
Solar Agri-Photovoltaics (Agri-PV) Dual-Income & Clean Energy Modeler.
Simulates dual land-use by mounting elevated (3.5m clearance) bifacial solar PV arrays
above shade-tolerant agricultural and agroforestry crops in Karnataka:
- Computes annual kWh electricity generation based on regional solar irradiance (GHI)
- Calculates PM-KUSUM Component A grid export earnings under Karnataka ESCOMs (₹3.15/kWh)
- Determines crop microclimate compatibility under 40% filtered agrivoltaic shade
- Computes combined dual-revenue: Crop Yield Return + Solar Tariff Cashflow
"""

# Regional Karnataka Annual Global Horizontal Irradiance (GHI in kWh/m2/day)
KARNATAKA_SOLAR_INSOLATION = {
    "North Karnataka": {"ghi": 5.75, "capacity_kwp_acre": 220, "annual_gen_kwh": 330000, "escom": "HESCOM / GESCOM"},
    "Central Karnataka": {"ghi": 5.50, "capacity_kwp_acre": 210, "annual_gen_kwh": 315000, "escom": "BESCOM / HESCOM"},
    "South Interior Karnataka": {"ghi": 5.25, "capacity_kwp_acre": 200, "annual_gen_kwh": 300000, "escom": "BESCOM / CESC"},
    "Coastal & Malnad": {"ghi": 4.85, "capacity_kwp_acre": 180, "annual_gen_kwh": 265000, "escom": "MESCOM"}
}

# Crop compatibility ratings under 35–45% filtered agrivoltaic canopy shade
SHADE_COMPATIBILITY = {
    "turmeric": {"compatibility": "Excellent (+15% Rhizome Yield)", "shade_effect": "Enhanced curcumin concentration and reduced sunburn leaf stress.", "fit_score": 95},
    "ginger": {"compatibility": "Excellent (+18% Yield)", "shade_effect": "Optimal cool root-zone microclimate and reduced evapotranspiration.", "fit_score": 96},
    "black pepper": {"compatibility": "Excellent", "shade_effect": "Ideal climbing vines under solar structural steel pillars.", "fit_score": 92},
    "cardamom": {"compatibility": "High", "shade_effect": "Matches Malnad understorey ambient light needs.", "fit_score": 88},
    "coffee": {"compatibility": "High", "shade_effect": "Substitutes traditional shade trees while providing renewable power.", "fit_score": 90},
    "vanilla": {"compatibility": "Excellent", "shade_effect": "Filtered solar diffuse light maximizes orchid vine flowering.", "fit_score": 94},
    "fodder": {"compatibility": "High", "shade_effect": "Shade-loving Napier / Stylosanthes grass thrives under solar panels.", "fit_score": 90},
    "ragi": {"compatibility": "Moderate", "shade_effect": "Slight yield adjustment (-8%), compensated +500% by solar grid export.", "fit_score": 75},
    "groundnut": {"compatibility": "Moderate", "shade_effect": "Maintains 90% baseline yield with 35% lower water needs.", "fit_score": 78},
    "pomegranate": {"compatibility": "High", "shade_effect": "Eliminates fruit skin scorching during severe Deccan summer peaks.", "fit_score": 85},
    "arecanut": {"compatibility": "Low (Height limit)", "shade_effect": "Tall mature palms exceed 3.5m clearance; suited for boundary arrays.", "fit_score": 45},
    "sugarcane": {"compatibility": "Low (Sun loving)", "shade_effect": "High C4 sunlight requirement; better for dedicated ground arrays.", "fit_score": 40}
}

def model_agri_pv_dual_income(species_name, latitude=13.0, crop_gross_revenue=150000, acres=1.0):
    """
    Computes solar energy generation, grid export tariff earnings, and combined dual farm revenue.
    """
    # Determine region based on latitude
    if latitude >= 15.5:
        region = "North Karnataka"
    elif latitude >= 13.8:
        region = "Central Karnataka"
    elif latitude <= 12.5 and (74.0 <= latitude <= 76.0):
        region = "Coastal & Malnad"
    else:
        region = "South Interior Karnataka"

    sol_info = KARNATAKA_SOLAR_INSOLATION[region]
    kwp_capacity = round(sol_info["capacity_kwp_acre"] * acres)
    annual_kwh = round(sol_info["annual_gen_kwh"] * acres)
    
    # PM-KUSUM Karnataka Grid Export Tariff (₹3.15 per kWh feed-in tariff)
    tariff_rate = 3.15
    annual_solar_revenue = round(annual_kwh * tariff_rate)

    # Assess crop shade compatibility
    s_clean = species_name.lower()
    comp_data = {"compatibility": "Good", "shade_effect": "Moderates midday leaf temperature and saves 30% soil moisture.", "fit_score": 80}
    for k in SHADE_COMPATIBILITY:
        if k in s_clean:
            comp_data = SHADE_COMPATIBILITY[k]
            break

    # Adjust crop revenue under shade
    shade_yield_factor = 1.15 if "Excellent" in comp_data["compatibility"] else 0.92 if "Moderate" in comp_data["compatibility"] else 1.0
    adjusted_crop_revenue = round(crop_gross_revenue * shade_yield_factor)
    total_dual_revenue = adjusted_crop_revenue + annual_solar_revenue

    # CO2 offsets (0.82 kg CO2e / kWh grid emission factor)
    annual_co2_offset_tons = round((annual_kwh * 0.82) / 1000.0, 1)

    return {
        "region": region,
        "acres": round(acres, 1),
        "solar_capacity_kwp": f"{kwp_capacity} kWp",
        "annual_clean_electricity_kwh": f"{annual_kwh:,} kWh",
        "escom_grid_partner": sol_info["escom"],
        "feed_in_tariff_rate": f"₹{tariff_rate} / unit (PM-KUSUM)",
        "annual_solar_revenue": annual_solar_revenue,
        "adjusted_crop_revenue": adjusted_crop_revenue,
        "total_dual_revenue": total_dual_revenue,
        "dual_revenue_multiplier": f"{round(total_dual_revenue / max(1, crop_gross_revenue), 1)}x",
        "crop_compatibility": comp_data["compatibility"],
        "microclimate_benefit": comp_data["shade_effect"],
        "co2_offset_tons_yr": f"{annual_co2_offset_tons} tCO₂e / yr",
        "capital_subsidy": "Up to 30% Central + 30% Karnataka state subsidy under PM-KUSUM Component A"
    }
