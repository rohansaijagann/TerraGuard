"""
Karnataka & Central Government Agricultural, Horticultural & Agroforestry Scheme Matcher.
Matches recommended botanical species, 4-tier canopy models, and farm locations to active government subsidies:
- Raita Siri Scheme (Millet direct income support)
- Krishi Bhagya (Farm ponds, polyhouse, drip systems)
- National Bamboo Mission (NBM)
- NABARD Agroforestry & Commercial Timber Subsidies
- PMKSY (Per Drop More Crop Drip Subsidies)
- MIDH (Horticulture & Spices Mission)
- National Beekeeping & Honey Mission (Pollination & Secondary Income)
"""

SCHEME_DATABASE = [
    {
        "id": "raita_siri",
        "name": "Raita Siri Millet Incentive Scheme",
        "name_kn": "ರೈತ ಸಿರಿ ಯೋಜನೆ (ಸಿರಿಧಾನ್ಯ ಪ್ರೋತ್ಸಾಹ ಧನ)",
        "department": "Karnataka Dept of Agriculture",
        "department_kn": "ಕರ್ನಾಟಕ ಕೃಷಿ ಇಲಾಖೆ",
        "financial_support": "₹10,000 per Hectare (Direct Bank Transfer / DBT)",
        "financial_support_kn": "ಪ್ರತಿ ಹೆಕ್ಟೇರ್‌ಗೆ ₹೧೦,೦೦೦ ನೇರ ನಗದು ವರ್ಗಾವಣೆ (DBT)",
        "subsidy_pct": "100% Direct Cash Support",
        "triggers": ["ragi", "finger millet", "jowar", "sorghum", "bajra", "pearl millet", "foxtail", "navane", "same", "little millet", "kodo", "haraka", "proso"],
        "eligibility": "Karnataka farmers registered on FRUITS portal cultivating minor millets.",
        "eligibility_kn": "ಫ್ರೂಟ್ಸ್ (FRUITS) ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ನೋಂದಾಯಿತ ಸಿರಿಧಾನ್ಯ ಬೆಳೆಯುವ ರೈತರು.",
        "portal_url": "https://fruits.karnataka.gov.in",
        "portal_label": "FRUITS Portal Karnataka",
        "icon": "fa-seedling",
        "badge_color": "#10b981"
    },
    {
        "id": "krishi_bhagya",
        "name": "Krishi Bhagya Dryland Livelihood Scheme",
        "name_kn": "ಕೃಷಿ ಭಾಗ್ಯ ಯೋಜನೆ (ಕೃಷಿ ಹೊಂಡ & ನೆರಳು ಪರದೆ)",
        "department": "Karnataka Dept of Agriculture",
        "department_kn": "ಕರ್ನಾಟಕ ಕೃಷಿ ಇಲಾಖೆ",
        "financial_support": "80%–90% Subsidy for Farm Ponds (Krishi Honda) + Diesel Pump + Polythene Lining",
        "financial_support_kn": "ಕೃಷಿ ಹೊಂಡ ನಿರ್ಮಾಣ, ಡೀಸೆಲ್ ಪಂಪ್ ಮತ್ತು ಪಾಲಿಥಿನ್ ಹೊದಿಕೆಗೆ ೮೦%-೯೦% ಸಹಾಯಧನ",
        "subsidy_pct": "Up to 90% Subsidy",
        "triggers": ["groundnut", "chickpea", "toor dal", "pigeon pea", "sunflower", "cotton", "maize", "safflower", "millet"],
        "eligibility": "Dryland & rainfed farmers across Northern/Southern Maidan taluks.",
        "eligibility_kn": "ಮಳೆಯಾಶ್ರಿತ ಒಣಭೂಮಿ ಪ್ರದೇಶದ ರೈತರು.",
        "portal_url": "https://raitamitra.karnataka.gov.in",
        "portal_label": "Raita Mitra Portal",
        "icon": "fa-water",
        "badge_color": "#3b82f6"
    },
    {
        "id": "pmksy_drip",
        "name": "PMKSY / Micro-Irrigation Drip & Sprinkler Scheme",
        "name_kn": "ಪ್ರಧಾನ ಮಂತ್ರಿ ಕೃಷಿ ಸಿಂಚಾಯಿ ಯೋಜನೆ (ಹನಿ ನೀರಾವರಿ)",
        "department": "Karnataka Dept of Horticulture & Agriculture",
        "department_kn": "ಕರ್ನಾಟಕ ತೋಟಗಾರಿಕೆ ಇಲಾಖೆ",
        "financial_support": "90% Subsidy for SC/ST Small Farmers; 75% Subsidy for General Farmers",
        "financial_support_kn": "ಪ.ಜಾ/ಪ.ಪಂ ಸಣ್ಣ ರೈತರಿಗೆ ೯೦%, ಸಾಮಾನ್ಯ ವರ್ಗಕ್ಕೆ ೭೫% ಹನಿ ನೀರಾವರಿ ಸಬ್ಸಿಡಿ",
        "subsidy_pct": "75% – 90% Subsidy",
        "triggers": ["arecanut", "coconut", "pomegranate", "mango", "guava", "sugarcane", "banana", "chilli", "coffee", "pepper", "turmeric", "ginger"],
        "eligibility": "All farmers with verified borewell/canal water source.",
        "eligibility_kn": "ಬೋರ್‌ವೆಲ್ ಅಥವಾ ನೀರಾವರಿ ಮೂಲವಿರುವ ಎಲ್ಲಾ ರೈತರು.",
        "portal_url": "https://pmksy.gov.in",
        "portal_label": "PMKSY Karnataka Portal",
        "icon": "fa-faucet-drip",
        "badge_color": "#0ea5e9"
    },
    {
        "id": "bamboo_mission",
        "name": "National Bamboo Mission (NBM Agroforestry)",
        "name_kn": "ರಾಷ್ಟ್ರೀಯ ಬಿದಿರು ಅಭಿಯಾನ (ಕೃಷಿ ಅರಣ್ಯ)",
        "department": "Karnataka Forest Dept & NBM",
        "department_kn": "ಕರ್ನಾಟಕ ಅರಣ್ಯ ಇಲಾಖೆ",
        "financial_support": "₹50,000 per Hectare (50% Subsidy on tissue-cultured saplings, pits & fencing)",
        "financial_support_kn": "ಬಿದಿರು ಸಸಿ, ನೆಡುವಿಕೆ ಮತ್ತು ಬೇಲಿಗೆ ಪ್ರತಿ ಹೆಕ್ಟೇರ್‌ಗೆ ₹೫೦,೦೦೦ (೫೦% ಸಹಾಯಧನ)",
        "subsidy_pct": "50% Capital Grant",
        "triggers": ["bamboo", "dendrocalamus", "bambusa"],
        "eligibility": "Farmers planting commercial bamboo varieties on farm bunds or block plantations.",
        "eligibility_kn": "ಜಮೀನಿನ ಬದುಗಳಲ್ಲಿ ಅಥವಾ ಪ್ಲಾಂಟೇಶನ್ ಮಾದರಿಯಲ್ಲಿ ಬಿದಿರು ಬೆಳೆಯುವ ರೈತರು.",
        "portal_url": "https://nbm.nic.in",
        "portal_label": "National Bamboo Mission",
        "icon": "fa-tree",
        "badge_color": "#059669"
    },
    {
        "id": "nabard_agroforestry",
        "name": "NABARD Tree Farming & Agroforestry Capital Subsidy",
        "name_kn": "ನಬಾರ್ಡ್ ಕೃಷಿ ಅರಣ್ಯ ಮತ್ತು ಮರಮಟ್ಟು ಸಬ್ಸಿಡಿ",
        "department": "NABARD & National Agroforestry Policy",
        "department_kn": "ನಬಾರ್ಡ್ ಮತ್ತು ಕೃಷಿ ಅರಣ್ಯ ನೀತಿ",
        "financial_support": "40% Capital Subsidy + 4% Concessional Refinance Loan for High-Value Timber",
        "financial_support_kn": "ಮರಮಟ್ಟು ಸಸಿ ನೆಡಲು ೪೦% ಬಂಡವಾಳ ಸಬ್ಸಿಡಿ ಮತ್ತು ೪% ಬಡ್ಡಿದರದ ಸಾಲ",
        "subsidy_pct": "40% Subsidy",
        "triggers": ["melia dubia", "malabar neem", "teak", "sandalwood", "rosewood", "silver oak", "neem", "acacia", "tamarind", "banyan", "pongamia", "honge"],
        "eligibility": "Landowners cultivating certified timber/plywood agroforestry models.",
        "eligibility_kn": "ವಾಣಿಜ್ಯ ಮರಮಟ್ಟು ಬೆಳೆಯುವ ಜಮೀನು ಮಾಲೀಕರು.",
        "portal_url": "https://www.nabard.org",
        "portal_label": "NABARD Official Portal",
        "icon": "fa-landmark",
        "badge_color": "#8b5cf6"
    },
    {
        "id": "midh_horticulture",
        "name": "MIDH Horticulture Mission (Fruit & Spice Orchards)",
        "name_kn": "ಸಮಗ್ರ ತೋಟಗಾರಿಕೆ ಅಭಿವೃದ್ಧಿ ಮಿಷನ್ (MIDH)",
        "department": "Karnataka Dept of Horticulture",
        "department_kn": "ಕರ್ನಾಟಕ ತೋಟಗಾರಿಕೆ ಇಲಾಖೆ",
        "financial_support": "40%–50% Subsidy on High-Density Planting, Trellising & Organic Certification",
        "financial_support_kn": "ಅಧಿಕ ಸಾಂದ್ರತೆಯ ತೋಟಗಾರಿಕೆ ಮತ್ತು ಸಾವಯವ ಪ್ರಮಾಣೀಕರಣಕ್ಕೆ ೪೦%-೫೦% ಸಹಾಯಧನ",
        "subsidy_pct": "40% – 50% Subsidy",
        "triggers": ["pomegranate", "mango", "guava", "sapota", "fig", "papaya", "black pepper", "cardamom", "clove", "nutmeg", "cinnamon", "avocado", "turmeric", "ginger", "garcinia"],
        "eligibility": "Farmers establishing new orchards or intercropping high-value spices.",
        "eligibility_kn": "ಹೊಸ ಹಣ್ಣಿನ ತೋಟ ಅಥವಾ ಸಾಂಬಾರು ಬೆಳೆ ಬೆಳೆಯುವ ರೈತರು.",
        "portal_url": "https://horticulture.karnataka.gov.in",
        "portal_label": "Karnataka Horticulture Dept",
        "icon": "fa-lemon",
        "badge_color": "#f59e0b"
    },
    {
        "id": "beekeeping_pollination",
        "name": "National Beekeeping & Honey Mission (NBHM)",
        "name_kn": "ರಾಷ್ಟ್ರೀಯ ಜೇನು ಕೃಷಿ ಅಭಿಯಾನ (ಪರಾಗಸ್ಪರ್ಶ & ಆದಾಯ)",
        "department": "National Bee Board (NBB)",
        "department_kn": "ರಾಷ್ಟ್ರೀಯ ಜೇನು ಅಭಿವೃದ್ಧಿ ಮಂಡಳಿ",
        "financial_support": "80% Subsidy on Beehive Boxes & Honey Extractors (₹4,000 per colony)",
        "financial_support_kn": "ಜೇನುಪೆಟ್ಟಿಗೆ ಮತ್ತು ಜೇನುತುಪ್ಪ ಉಪಕರಣಗಳಿಗೆ ೮೦% ಸಹಾಯಧನ",
        "subsidy_pct": "80% Subsidy",
        "triggers": ["coffee", "sunflower", "mustard", "mango", "moringa", "guava", "cardamom", "multi-crop"],
        "eligibility": "Farmers integrating apiaries in agroforestry/orchards to boost crop pollination.",
        "eligibility_kn": "ಪರಾಗಸ್ಪರ್ಶ ಹೆಚ್ಚಿಸಲು ಜಮೀನಿನಲ್ಲಿ ಜೇನುಪೆಟ್ಟಿಗೆ ಇಡುವ ರೈತರು.",
        "portal_url": "https://nbb.gov.in",
        "portal_label": "National Bee Board",
        "icon": "fa-cubes-stacked",
        "badge_color": "#eab308"
    }
]

def match_government_schemes(species_name, agro_zone=""):
    """
    Evaluates candidate species and returns all matching Karnataka & Central Government schemes.
    """
    s_clean = (species_name or "").lower()
    matches = []

    for scheme in SCHEME_DATABASE:
        is_matched = any(trig in s_clean for trig in scheme["triggers"])
        if is_matched:
            matches.append({
                "id": scheme["id"],
                "name": scheme["name"],
                "name_kn": scheme["name_kn"],
                "department": scheme["department"],
                "department_kn": scheme["department_kn"],
                "financial_support": scheme["financial_support"],
                "financial_support_kn": scheme["financial_support_kn"],
                "subsidy_pct": scheme["subsidy_pct"],
                "eligibility": scheme["eligibility"],
                "eligibility_kn": scheme["eligibility_kn"],
                "portal_url": scheme["portal_url"],
                "portal_label": scheme["portal_label"],
                "icon": scheme["icon"],
                "badge_color": scheme["badge_color"]
            })

    # Default general PMKSY drip subsidy if no specific crop scheme matched
    if not matches:
        pmksy = SCHEME_DATABASE[2] # PMKSY
        matches.append({
            "id": pmksy["id"],
            "name": pmksy["name"],
            "name_kn": pmksy["name_kn"],
            "department": pmksy["department"],
            "department_kn": pmksy["department_kn"],
            "financial_support": pmksy["financial_support"],
            "financial_support_kn": pmksy["financial_support_kn"],
            "subsidy_pct": pmksy["subsidy_pct"],
            "eligibility": pmksy["eligibility"],
            "eligibility_kn": pmksy["eligibility_kn"],
            "portal_url": pmksy["portal_url"],
            "portal_label": pmksy["portal_label"],
            "icon": pmksy["icon"],
            "badge_color": pmksy["badge_color"]
        })

    return matches
