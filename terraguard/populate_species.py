import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'terraguard.settings')
django.setup()

from decision_support.models import KarnatakaAgroZone, SpeciesConstraint

# Fetch or create the 4 Agro Zones
coastal_zone, _ = KarnatakaAgroZone.objects.get_or_create(
    name='Coastal (Karavali)',
    defaults={'soil_profile': 'Lateritic & Coastal Alluvium', 'min_rainfall_mm': 2500, 'max_rainfall_mm': 4500, 'base_elevation_m': 50}
)

malnad_zone, _ = KarnatakaAgroZone.objects.get_or_create(
    name='Western Ghats (Malnad)',
    defaults={'soil_profile': 'Humus Forest Loam & Clay', 'min_rainfall_mm': 1500, 'max_rainfall_mm': 3500, 'base_elevation_m': 900}
)

north_maidan, _ = KarnatakaAgroZone.objects.get_or_create(
    name='Northern Maidan',
    defaults={'soil_profile': 'Deep Black Cotton & Vertisols', 'min_rainfall_mm': 400, 'max_rainfall_mm': 850, 'base_elevation_m': 500}
)

south_maidan, _ = KarnatakaAgroZone.objects.get_or_create(
    name='Southern Maidan',
    defaults={'soil_profile': 'Red Sandy Loam & Lateritic Gravel', 'min_rainfall_mm': 600, 'max_rainfall_mm': 1100, 'base_elevation_m': 800}
)

SPECIES_DATA = [
    # ══ 1. COASTAL (KARAVALI) ZONE ══
    # Crops
    {"name": "Paddy (Coastal Pokkali)", "type": "CROP", "zone": coastal_zone, "drought": 3, "ph_min": 5.0, "ph_max": 7.2, "elev_min": 0, "elev_max": 300, "t_min": 22, "t_max": 36, "carbon": 4, "comm": "Medium - Salt-Tolerant Staple Red Rice"},
    {"name": "Paddy (Jyothi / Panchami)", "type": "CROP", "zone": coastal_zone, "drought": 4, "ph_min": 5.2, "ph_max": 7.0, "elev_min": 0, "elev_max": 400, "t_min": 22, "t_max": 35, "carbon": 4, "comm": "High - Premium High-Yielding Coastal Rice"},
    {"name": "Cocoa (Forastero)", "type": "CROP", "zone": coastal_zone, "drought": 5, "ph_min": 5.5, "ph_max": 7.0, "elev_min": 0, "elev_max": 500, "t_min": 20, "t_max": 34, "carbon": 6, "comm": "High - Confectionery & Global Export"},
    {"name": "Vanilla (Planifolia)", "type": "CROP", "zone": coastal_zone, "drought": 3, "ph_min": 5.5, "ph_max": 6.8, "elev_min": 50, "elev_max": 700, "t_min": 21, "t_max": 32, "carbon": 4, "comm": "Very High - Ultra-Premium Natural Flavouring Spice"},
    {"name": "Pineapple (Giant Kew)", "type": "CROP", "zone": coastal_zone, "drought": 6, "ph_min": 4.5, "ph_max": 6.5, "elev_min": 0, "elev_max": 600, "t_min": 20, "t_max": 35, "carbon": 4, "comm": "High - Commercial Fruit & Canning Processing"},
    {"name": "Betelvine (Kariyele)", "type": "CROP", "zone": coastal_zone, "drought": 4, "ph_min": 6.0, "ph_max": 7.5, "elev_min": 0, "elev_max": 400, "t_min": 22, "t_max": 33, "carbon": 3, "comm": "High - High Daily Cash-Flow Cultural Crop"},
    {"name": "Tapioca (Cassava)", "type": "CROP", "zone": coastal_zone, "drought": 7, "ph_min": 4.5, "ph_max": 7.2, "elev_min": 0, "elev_max": 500, "t_min": 22, "t_max": 38, "carbon": 5, "comm": "Medium - Industrial Starch & Food Security"},
    {"name": "Black Pepper (Panniyur-1)", "type": "CROP", "zone": coastal_zone, "drought": 4, "ph_min": 5.0, "ph_max": 6.5, "elev_min": 20, "elev_max": 800, "t_min": 20, "t_max": 33, "carbon": 5, "comm": "Very High - Black Gold Export Spice"},
    {"name": "Ginger (Rio-de-Janeiro)", "type": "CROP", "zone": coastal_zone, "drought": 4, "ph_min": 5.5, "ph_max": 6.8, "elev_min": 0, "elev_max": 600, "t_min": 22, "t_max": 34, "carbon": 3, "comm": "High - Culinary Spice & Medicinal Essential Oil"},
    {"name": "Turmeric (Alleppey)", "type": "CROP", "zone": coastal_zone, "drought": 5, "ph_min": 5.2, "ph_max": 7.0, "elev_min": 0, "elev_max": 600, "t_min": 22, "t_max": 35, "carbon": 4, "comm": "High - High Curcumin Golden Spice"},
    {"name": "Udupi Mattu Gulla (Brinjal)", "type": "CROP", "zone": coastal_zone, "drought": 4, "ph_min": 5.5, "ph_max": 7.0, "elev_min": 0, "elev_max": 200, "t_min": 22, "t_max": 35, "carbon": 3, "comm": "High - GI Tagged Specialty Gourmet Vegetable"},
    {"name": "Watermelon (Sugar Baby)", "type": "CROP", "zone": coastal_zone, "drought": 6, "ph_min": 5.8, "ph_max": 7.2, "elev_min": 0, "elev_max": 300, "t_min": 24, "t_max": 38, "carbon": 3, "comm": "Medium - Summer Refreshment Cash Crop"},
    # Trees
    {"name": "Coconut (West Coast Tall)", "type": "TREE", "zone": coastal_zone, "drought": 6, "ph_min": 5.2, "ph_max": 8.0, "elev_min": 0, "elev_max": 600, "t_min": 22, "t_max": 36, "carbon": 8, "comm": "Very High - Kalpavriksha Copra & Neera"},
    {"name": "Arecanut (South Kanara Local)", "type": "TREE", "zone": coastal_zone, "drought": 5, "ph_min": 5.0, "ph_max": 7.0, "elev_min": 0, "elev_max": 600, "t_min": 20, "t_max": 34, "carbon": 7, "comm": "Very High - Prime Commercial Nut Cash Crop"},
    {"name": "Cashew (Vengurla-4)", "type": "TREE", "zone": coastal_zone, "drought": 8, "ph_min": 4.8, "ph_max": 7.2, "elev_min": 0, "elev_max": 500, "t_min": 22, "t_max": 38, "carbon": 7, "comm": "Very High - Global Cashew Kernel Export"},
    {"name": "Rubber (RRII-105)", "type": "TREE", "zone": coastal_zone, "drought": 4, "ph_min": 4.5, "ph_max": 6.0, "elev_min": 0, "elev_max": 400, "t_min": 22, "t_max": 35, "carbon": 9, "comm": "High - Industrial Latex & Timber"},
    {"name": "Nutmeg (IISR Viswashree)", "type": "TREE", "zone": coastal_zone, "drought": 4, "ph_min": 5.5, "ph_max": 6.8, "elev_min": 20, "elev_max": 600, "t_min": 20, "t_max": 33, "carbon": 7, "comm": "High - Nutmeg & Mace Twin Export Spice"},
    {"name": "Clove (Zanzibar)", "type": "TREE", "zone": coastal_zone, "drought": 4, "ph_min": 5.0, "ph_max": 6.5, "elev_min": 50, "elev_max": 700, "t_min": 20, "t_max": 32, "carbon": 7, "comm": "High - Essential Oil & Culinary Aromatic"},
    {"name": "Cinnamon (Navashree)", "type": "TREE", "zone": coastal_zone, "drought": 5, "ph_min": 5.0, "ph_max": 6.8, "elev_min": 0, "elev_max": 700, "t_min": 20, "t_max": 34, "carbon": 7, "comm": "High - Pure Quills Bark Spice"},
    {"name": "Kokum (Garcinia indica)", "type": "TREE", "zone": coastal_zone, "drought": 6, "ph_min": 4.8, "ph_max": 6.8, "elev_min": 0, "elev_max": 600, "t_min": 20, "t_max": 36, "carbon": 7, "comm": "High - Nutraceutical HCA & Cooling Butter"},
    {"name": "Mangosteen", "type": "TREE", "zone": coastal_zone, "drought": 3, "ph_min": 5.0, "ph_max": 6.5, "elev_min": 20, "elev_max": 500, "t_min": 22, "t_max": 34, "carbon": 8, "comm": "Very High - Queen of Fruits Exotic Luxury"},
    {"name": "Rambutan (Malwana)", "type": "TREE", "zone": coastal_zone, "drought": 4, "ph_min": 5.2, "ph_max": 6.5, "elev_min": 10, "elev_max": 400, "t_min": 22, "t_max": 35, "carbon": 7, "comm": "High - Exotic Tropical Dessert Fruit"},
    {"name": "Casuarina (Sarve Mara)", "type": "TREE", "zone": coastal_zone, "drought": 8, "ph_min": 5.0, "ph_max": 8.2, "elev_min": 0, "elev_max": 400, "t_min": 20, "t_max": 40, "carbon": 9, "comm": "High - Coastal Windbreak Poles & Paper Pulp"},
    {"name": "Acacia Mangium", "type": "TREE", "zone": coastal_zone, "drought": 7, "ph_min": 4.5, "ph_max": 6.5, "elev_min": 0, "elev_max": 500, "t_min": 20, "t_max": 38, "carbon": 9, "comm": "High - Fast-Growing Timber & Plywood"},
    {"name": "Bamboo (Bambusa balcooa)", "type": "TREE", "zone": coastal_zone, "drought": 7, "ph_min": 5.0, "ph_max": 7.5, "elev_min": 0, "elev_max": 800, "t_min": 18, "t_max": 38, "carbon": 10, "comm": "High - Green Gold Biomass & Structural Timber"},
    {"name": "Jackfruit (Tubagere)", "type": "TREE", "zone": coastal_zone, "drought": 7, "ph_min": 5.2, "ph_max": 7.2, "elev_min": 0, "elev_max": 700, "t_min": 18, "t_max": 36, "carbon": 8, "comm": "High - Superfood Vegan Meat & Wood"},

    # ══ 2. WESTERN GHATS (MALNAD) ZONE ══
    # Crops
    {"name": "Coffee Arabica (S-795)", "type": "CROP", "zone": malnad_zone, "drought": 5, "ph_min": 5.2, "ph_max": 6.5, "elev_min": 800, "elev_max": 1600, "t_min": 15, "t_max": 28, "carbon": 6, "comm": "Very High - Specialty Plantation Coffee"},
    {"name": "Coffee Robusta (CxR)", "type": "CROP", "zone": malnad_zone, "drought": 6, "ph_min": 5.0, "ph_max": 6.8, "elev_min": 500, "elev_max": 1100, "t_min": 18, "t_max": 32, "carbon": 6, "comm": "High - Robust High-Yielding Commercial Coffee"},
    {"name": "Cardamom (Njallani)", "type": "CROP", "zone": malnad_zone, "drought": 3, "ph_min": 4.8, "ph_max": 6.2, "elev_min": 700, "elev_max": 1400, "t_min": 14, "t_max": 28, "carbon": 5, "comm": "Very High - Queen of Spices Global Export"},
    {"name": "Tea (Camellia sinensis)", "type": "CROP", "zone": malnad_zone, "drought": 4, "ph_min": 4.5, "ph_max": 5.8, "elev_min": 900, "elev_max": 1800, "t_min": 12, "t_max": 26, "carbon": 6, "comm": "High - High-Altitude CTC & Orthodox Tea"},
    {"name": "Black Pepper (Karimunda)", "type": "CROP", "zone": malnad_zone, "drought": 4, "ph_min": 5.2, "ph_max": 6.5, "elev_min": 400, "elev_max": 1200, "t_min": 18, "t_max": 30, "carbon": 5, "comm": "Very High - High Piperine Forest Pepper"},
    {"name": "Bird's Eye Chilli (Kanthari)", "type": "CROP", "zone": malnad_zone, "drought": 6, "ph_min": 5.5, "ph_max": 6.8, "elev_min": 400, "elev_max": 1200, "t_min": 16, "t_max": 32, "carbon": 3, "comm": "High - High Capsaicin Medicinal Hot Chilli"},
    {"name": "Malnad Ginger (Mahima)", "type": "CROP", "zone": malnad_zone, "drought": 4, "ph_min": 5.5, "ph_max": 6.5, "elev_min": 500, "elev_max": 1100, "t_min": 18, "t_max": 30, "carbon": 4, "comm": "High - Plump Rhizome Commercial Ginger"},
    {"name": "Turmeric (Pragati)", "type": "CROP", "zone": malnad_zone, "drought": 5, "ph_min": 5.2, "ph_max": 6.8, "elev_min": 400, "elev_max": 1000, "t_min": 18, "t_max": 32, "carbon": 4, "comm": "High - High Curcumin Shade-Tolerant Rhizome"},
    {"name": "Passion Fruit (Kaveri)", "type": "CROP", "zone": malnad_zone, "drought": 5, "ph_min": 5.5, "ph_max": 6.5, "elev_min": 600, "elev_max": 1400, "t_min": 15, "t_max": 28, "carbon": 4, "comm": "High - Aromatic Juice & Squash Processing"},
    {"name": "Strawberry (Sweet Charlie)", "type": "CROP", "zone": malnad_zone, "drought": 3, "ph_min": 5.5, "ph_max": 6.5, "elev_min": 900, "elev_max": 1600, "t_min": 10, "t_max": 25, "carbon": 3, "comm": "Very High - Cold-Climate Luxury Dessert Berry"},
    {"name": "Rajamudi Red Rice", "type": "CROP", "zone": malnad_zone, "drought": 4, "ph_min": 5.0, "ph_max": 6.5, "elev_min": 500, "elev_max": 1000, "t_min": 18, "t_max": 32, "carbon": 4, "comm": "High - Royal Heritage Nutritious Rice"},
    # Trees & Timber
    {"name": "Silver Oak (Grevillea)", "type": "TREE", "zone": malnad_zone, "drought": 7, "ph_min": 5.0, "ph_max": 7.0, "elev_min": 600, "elev_max": 1600, "t_min": 12, "t_max": 30, "carbon": 9, "comm": "High - Ideal Coffee Shade & Timber"},
    {"name": "Sandalwood (Srigandha)", "type": "TREE", "zone": malnad_zone, "drought": 8, "ph_min": 6.0, "ph_max": 7.8, "elev_min": 400, "elev_max": 1200, "t_min": 15, "t_max": 36, "carbon": 8, "comm": "Ultra High - Crown Jewel Heartwood & Oil"},
    {"name": "Rosewood (Dalbergia latifolia)", "type": "TREE", "zone": malnad_zone, "drought": 7, "ph_min": 5.5, "ph_max": 7.0, "elev_min": 300, "elev_max": 1100, "t_min": 16, "t_max": 34, "carbon": 10, "comm": "Ultra High - Elite Luxury Furniture Timber"},
    {"name": "Teak (Tectona grandis)", "type": "TREE", "zone": malnad_zone, "drought": 7, "ph_min": 6.0, "ph_max": 7.5, "elev_min": 200, "elev_max": 900, "t_min": 18, "t_max": 38, "carbon": 9, "comm": "Very High - Golden Standard Building Timber"},
    {"name": "Honne (Malabar Kino)", "type": "TREE", "zone": malnad_zone, "drought": 7, "ph_min": 5.5, "ph_max": 7.0, "elev_min": 300, "elev_max": 1000, "t_min": 16, "t_max": 35, "carbon": 9, "comm": "Very High - Heavy Construction & Sacred Wood"},
    {"name": "Melia Dubia (Hebbevu)", "type": "TREE", "zone": malnad_zone, "drought": 7, "ph_min": 5.5, "ph_max": 7.5, "elev_min": 300, "elev_max": 1200, "t_min": 16, "t_max": 38, "carbon": 10, "comm": "High - Fast 6-Year Plywood Rotation Timber"},
    {"name": "Mahogany (Swietenia)", "type": "TREE", "zone": malnad_zone, "drought": 6, "ph_min": 5.5, "ph_max": 7.0, "elev_min": 300, "elev_max": 1000, "t_min": 18, "t_max": 35, "carbon": 9, "comm": "High - Commercial Hardwood Timber"},
    {"name": "Avocado (Hass / Butter Fruit)", "type": "TREE", "zone": malnad_zone, "drought": 5, "ph_min": 5.5, "ph_max": 6.8, "elev_min": 700, "elev_max": 1500, "t_min": 14, "t_max": 28, "carbon": 8, "comm": "Very High - Global Superfood Healthy Lipid Fruit"},
    {"name": "Allspice (Pimenta dioica)", "type": "TREE", "zone": malnad_zone, "drought": 5, "ph_min": 5.5, "ph_max": 6.8, "elev_min": 500, "elev_max": 1200, "t_min": 16, "t_max": 30, "carbon": 7, "comm": "High - 4-in-1 Fragrant Culinary Spice"},
    {"name": "Kadamba (Neolamarckia)", "type": "TREE", "zone": malnad_zone, "drought": 5, "ph_min": 5.0, "ph_max": 7.0, "elev_min": 200, "elev_max": 900, "t_min": 18, "t_max": 36, "carbon": 9, "comm": "High - Rapid Biomass & Sacred Ornamental Wood"},
    {"name": "Red Sanders (Rakta Chandana)", "type": "TREE", "zone": malnad_zone, "drought": 8, "ph_min": 6.0, "ph_max": 7.8, "elev_min": 300, "elev_max": 800, "t_min": 18, "t_max": 38, "carbon": 9, "comm": "Ultra High - Export Grade Red Wood & Dye"},
    {"name": "Bamboo (Dendrocalamus)", "type": "TREE", "zone": malnad_zone, "drought": 7, "ph_min": 5.0, "ph_max": 7.2, "elev_min": 300, "elev_max": 1200, "t_min": 15, "t_max": 36, "carbon": 10, "comm": "High - Heavy Solid Structural Giant Bamboo"},

    # ══ 3. NORTHERN MAIDAN ZONE ══
    # Crops
    {"name": "Bt Cotton (Bollgard II)", "type": "CROP", "zone": north_maidan, "drought": 7, "ph_min": 6.5, "ph_max": 8.5, "elev_min": 300, "elev_max": 700, "t_min": 20, "t_max": 40, "carbon": 5, "comm": "High - White Gold Textile Industrial Fiber"},
    {"name": "Desi Cotton (Jayadhar)", "type": "CROP", "zone": north_maidan, "drought": 9, "ph_min": 6.5, "ph_max": 8.5, "elev_min": 300, "elev_max": 700, "t_min": 20, "t_max": 42, "carbon": 5, "comm": "High - Drought-Proof Organic Short-Staple"},
    {"name": "Jowar (Maldandi M 35-1)", "type": "CROP", "zone": north_maidan, "drought": 9, "ph_min": 6.0, "ph_max": 8.5, "elev_min": 350, "elev_max": 750, "t_min": 18, "t_max": 38, "carbon": 5, "comm": "High - Premium Rabi Sweet Sorghum Roti Grain"},
    {"name": "Hybrid Jowar (CSH-16)", "type": "CROP", "zone": north_maidan, "drought": 8, "ph_min": 6.2, "ph_max": 8.5, "elev_min": 350, "elev_max": 750, "t_min": 20, "t_max": 40, "carbon": 5, "comm": "Medium - High-Yielding Kharif Grain & Stover"},
    {"name": "Bajra (Pearl Millet)", "type": "CROP", "zone": north_maidan, "drought": 9, "ph_min": 6.5, "ph_max": 8.5, "elev_min": 300, "elev_max": 700, "t_min": 22, "t_max": 42, "carbon": 5, "comm": "High - Nutri-Cereal Climate-Resilient Millet"},
    {"name": "Wheat (DWR-162 / Lok-1)", "type": "CROP", "zone": north_maidan, "drought": 6, "ph_min": 6.5, "ph_max": 8.2, "elev_min": 400, "elev_max": 750, "t_min": 12, "t_max": 30, "carbon": 4, "comm": "High - Essential Food Security Bread Wheat"},
    {"name": "Durum Wheat (Bijaga Yellow)", "type": "CROP", "zone": north_maidan, "drought": 7, "ph_min": 6.8, "ph_max": 8.4, "elev_min": 400, "elev_max": 750, "t_min": 14, "t_max": 32, "carbon": 4, "comm": "High - High Protein Pasta & Semolina Wheat"},
    {"name": "Toor Dal (GRG-811 / TS-3R)", "type": "CROP", "zone": north_maidan, "drought": 8, "ph_min": 6.5, "ph_max": 8.5, "elev_min": 350, "elev_max": 700, "t_min": 20, "t_max": 38, "carbon": 6, "comm": "High - GI Tagged Gulbarga Red Gram Protein Pulse"},
    {"name": "Chickpea (JG-11 / Annigeri)", "type": "CROP", "zone": north_maidan, "drought": 8, "ph_min": 6.5, "ph_max": 8.5, "elev_min": 400, "elev_max": 800, "t_min": 12, "t_max": 30, "carbon": 5, "comm": "High - Major Rabi Bengal Gram Protein Pulse"},
    {"name": "Green Gram (Shiny Moong)", "type": "CROP", "zone": north_maidan, "drought": 7, "ph_min": 6.2, "ph_max": 8.0, "elev_min": 350, "elev_max": 700, "t_min": 22, "t_max": 38, "carbon": 5, "comm": "High - 65-Day Short Duration Catch Crop"},
    {"name": "Black Gram (LBG-625)", "type": "CROP", "zone": north_maidan, "drought": 7, "ph_min": 6.2, "ph_max": 8.0, "elev_min": 350, "elev_max": 700, "t_min": 22, "t_max": 38, "carbon": 5, "comm": "High - Essential Urad Dosa Batter Pulse"},
    {"name": "Soybean (JS-335 / DSb-21)", "type": "CROP", "zone": north_maidan, "drought": 6, "ph_min": 6.0, "ph_max": 7.8, "elev_min": 400, "elev_max": 800, "t_min": 20, "t_max": 35, "carbon": 6, "comm": "High - Oilseed & Animal Feed Soya Meal"},
    {"name": "Groundnut (GPBD-4)", "type": "CROP", "zone": north_maidan, "drought": 7, "ph_min": 6.0, "ph_max": 7.8, "elev_min": 350, "elev_max": 750, "t_min": 20, "t_max": 36, "carbon": 5, "comm": "High - High Oil Peanut & Edible Cake"},
    {"name": "Sunflower (KBSH-44)", "type": "CROP", "zone": north_maidan, "drought": 7, "ph_min": 6.5, "ph_max": 8.2, "elev_min": 350, "elev_max": 750, "t_min": 18, "t_max": 36, "carbon": 4, "comm": "High - Premium Edible Heart-Healthy Oilseed"},
    {"name": "Safflower (Kusube)", "type": "CROP", "zone": north_maidan, "drought": 9, "ph_min": 6.8, "ph_max": 8.5, "elev_min": 400, "elev_max": 800, "t_min": 14, "t_max": 34, "carbon": 5, "comm": "High - Deep-Rooted Drought Resistant Oilseed"},
    {"name": "Sesame (White Til)", "type": "CROP", "zone": north_maidan, "drought": 8, "ph_min": 6.2, "ph_max": 7.8, "elev_min": 350, "elev_max": 700, "t_min": 22, "t_max": 38, "carbon": 4, "comm": "High - Premium Confectionery & Export Sesame"},
    {"name": "Byadagi Chilli (Kaddi)", "type": "CROP", "zone": north_maidan, "drought": 7, "ph_min": 6.2, "ph_max": 8.0, "elev_min": 400, "elev_max": 700, "t_min": 20, "t_max": 36, "carbon": 4, "comm": "Very High - GI Tagged Deep Red Oleoresin Spice"},
    {"name": "Bellary Onion (Arka Kalyan)", "type": "CROP", "zone": north_maidan, "drought": 6, "ph_min": 6.5, "ph_max": 8.0, "elev_min": 350, "elev_max": 700, "t_min": 16, "t_max": 34, "carbon": 3, "comm": "High - Major Commercial Export Bulb Crop"},
    {"name": "Garlic (G-282)", "type": "CROP", "zone": north_maidan, "drought": 6, "ph_min": 6.5, "ph_max": 8.0, "elev_min": 400, "elev_max": 750, "t_min": 14, "t_max": 30, "carbon": 3, "comm": "High - High Allicin Medicinal Culinary Bulb"},
    {"name": "Maize (Kargil-900M)", "type": "CROP", "zone": north_maidan, "drought": 6, "ph_min": 6.0, "ph_max": 7.8, "elev_min": 350, "elev_max": 750, "t_min": 20, "t_max": 36, "carbon": 5, "comm": "High - Starch Industry & Poultry Feed Maize"},
    {"name": "Sugarcane (Co 86032)", "type": "CROP", "zone": north_maidan, "drought": 5, "ph_min": 6.5, "ph_max": 8.2, "elev_min": 350, "elev_max": 650, "t_min": 22, "t_max": 38, "carbon": 7, "comm": "High - High Sucrose Sugar Mill Cash Crop"},
    {"name": "Navane (Foxtail Millet)", "type": "CROP", "zone": north_maidan, "drought": 9, "ph_min": 6.0, "ph_max": 8.2, "elev_min": 350, "elev_max": 750, "t_min": 20, "t_max": 38, "carbon": 4, "comm": "High - Diabetic-Friendly Siridhanya Millet"},
    {"name": "Same (Little Millet)", "type": "CROP", "zone": north_maidan, "drought": 9, "ph_min": 5.8, "ph_max": 8.0, "elev_min": 350, "elev_max": 750, "t_min": 20, "t_max": 38, "carbon": 4, "comm": "High - Fast 75-Day Superfood Ancient Grain"},
    # Trees & Horticulture
    {"name": "Pomegranate (Bhagwa)", "type": "TREE", "zone": north_maidan, "drought": 8, "ph_min": 6.5, "ph_max": 8.5, "elev_min": 350, "elev_max": 750, "t_min": 18, "t_max": 38, "carbon": 6, "comm": "Very High - Deep Red Aril Export Pomegranate"},
    {"name": "Grapes (Thompson Seedless)", "type": "CROP", "zone": north_maidan, "drought": 7, "ph_min": 6.5, "ph_max": 8.4, "elev_min": 400, "elev_max": 700, "t_min": 15, "t_max": 36, "carbon": 5, "comm": "Very High - Table Grape & Golden Raisin Production"},
    {"name": "Fig (Poona Anjeer)", "type": "TREE", "zone": north_maidan, "drought": 8, "ph_min": 6.8, "ph_max": 8.5, "elev_min": 400, "elev_max": 750, "t_min": 16, "t_max": 38, "carbon": 6, "comm": "High - High Iron Fresh & Dried Fruit"},
    {"name": "Acid Lime (Kagzi Balaji)", "type": "TREE", "zone": north_maidan, "drought": 7, "ph_min": 6.5, "ph_max": 8.2, "elev_min": 350, "elev_max": 700, "t_min": 18, "t_max": 40, "carbon": 6, "comm": "High - Year-Round High Citric Juice Lime"},
    {"name": "Sweet Orange (Mosambi)", "type": "TREE", "zone": north_maidan, "drought": 7, "ph_min": 6.5, "ph_max": 8.2, "elev_min": 350, "elev_max": 700, "t_min": 18, "t_max": 38, "carbon": 6, "comm": "High - Sweet Table Citrus & Commercial Juice"},
    {"name": "Ber (Umran / Gola)", "type": "TREE", "zone": north_maidan, "drought": 10, "ph_min": 6.5, "ph_max": 8.8, "elev_min": 300, "elev_max": 700, "t_min": 18, "t_max": 44, "carbon": 6, "comm": "Medium - Arid Zone Poor Man's Apple"},
    {"name": "Custard Apple (Arka Sahan)", "type": "TREE", "zone": north_maidan, "drought": 9, "ph_min": 6.0, "ph_max": 8.2, "elev_min": 350, "elev_max": 800, "t_min": 18, "t_max": 40, "carbon": 6, "comm": "High - High Sugar Creamy Dessert Fruit"},
    {"name": "Tamarind (PKM-1 Sweet)", "type": "TREE", "zone": north_maidan, "drought": 9, "ph_min": 5.5, "ph_max": 8.5, "elev_min": 300, "elev_max": 800, "t_min": 18, "t_max": 42, "carbon": 8, "comm": "High - Long-Life Processing Paste & Wood"},
    {"name": "Neem (Azadirachta indica)", "type": "TREE", "zone": north_maidan, "drought": 10, "ph_min": 6.0, "ph_max": 8.8, "elev_min": 200, "elev_max": 800, "t_min": 18, "t_max": 45, "carbon": 9, "comm": "High - Bio-Pesticide Azadirachtin & Timber"},
    {"name": "Acacia (Babul)", "type": "TREE", "zone": north_maidan, "drought": 10, "ph_min": 6.5, "ph_max": 9.0, "elev_min": 200, "elev_max": 800, "t_min": 18, "t_max": 46, "carbon": 8, "comm": "Medium - Extreme Drought Fodder & Charcoal"},

    # ══ 4. SOUTHERN MAIDAN & TRANSITION ZONE ══
    # Crops
    {"name": "Ragi (GPU-28 / ML-365)", "type": "CROP", "zone": south_maidan, "drought": 8, "ph_min": 5.5, "ph_max": 7.5, "elev_min": 600, "elev_max": 1000, "t_min": 18, "t_max": 34, "carbon": 5, "comm": "High - Golden Finger Millet Calcium Superfood"},
    {"name": "Ragi (Indaf-5)", "type": "CROP", "zone": south_maidan, "drought": 8, "ph_min": 5.5, "ph_max": 7.5, "elev_min": 600, "elev_max": 1000, "t_min": 18, "t_max": 34, "carbon": 5, "comm": "High - Traditional Drought-Hardy Millet"},
    {"name": "Paddy (Sona Masoori)", "type": "CROP", "zone": south_maidan, "drought": 5, "ph_min": 5.8, "ph_max": 7.5, "elev_min": 500, "elev_max": 900, "t_min": 20, "t_max": 35, "carbon": 4, "comm": "Very High - Light Aromatic Table Rice"},
    {"name": "Paddy (IR-64 / Jaya)", "type": "CROP", "zone": south_maidan, "drought": 5, "ph_min": 5.5, "ph_max": 7.5, "elev_min": 500, "elev_max": 900, "t_min": 20, "t_max": 35, "carbon": 4, "comm": "High - High-Yielding Commercial Rice"},
    {"name": "Maize (DKC-9108)", "type": "CROP", "zone": south_maidan, "drought": 6, "ph_min": 5.8, "ph_max": 7.5, "elev_min": 600, "elev_max": 1000, "t_min": 18, "t_max": 35, "carbon": 5, "comm": "High - Commercial Single Cross Hybrid Maize"},
    {"name": "Groundnut (TMV-2)", "type": "CROP", "zone": south_maidan, "drought": 7, "ph_min": 5.5, "ph_max": 7.2, "elev_min": 600, "elev_max": 950, "t_min": 20, "t_max": 34, "carbon": 5, "comm": "High - Red Soil Bunch Peanut"},
    {"name": "Horse Gram (Huruli PHG-9)", "type": "CROP", "zone": south_maidan, "drought": 9, "ph_min": 5.2, "ph_max": 7.5, "elev_min": 600, "elev_max": 1000, "t_min": 18, "t_max": 36, "carbon": 5, "comm": "High - Drought Hardy Protein & Fodder Legume"},
    {"name": "Field Bean (Avarekalu HA-4)", "type": "CROP", "zone": south_maidan, "drought": 7, "ph_min": 5.8, "ph_max": 7.5, "elev_min": 600, "elev_max": 1000, "t_min": 16, "t_max": 32, "carbon": 4, "comm": "Very High - Cultural Winter Delicacy Broad Bean"},
    {"name": "Cowpea (Alsande C-152)", "type": "CROP", "zone": south_maidan, "drought": 8, "ph_min": 5.5, "ph_max": 7.5, "elev_min": 600, "elev_max": 1000, "t_min": 20, "t_max": 35, "carbon": 5, "comm": "High - Dual Purpose Green Pod & Dry Pulse"},
    {"name": "Sugarcane (Mandya Co 62175)", "type": "CROP", "zone": south_maidan, "drought": 6, "ph_min": 6.0, "ph_max": 7.8, "elev_min": 550, "elev_max": 800, "t_min": 20, "t_max": 36, "carbon": 7, "comm": "High - Cauvery Basin Jaggery & Sugar Cane"},
    {"name": "Tobacco (FCV Special)", "type": "CROP", "zone": south_maidan, "drought": 7, "ph_min": 5.5, "ph_max": 6.8, "elev_min": 600, "elev_max": 900, "t_min": 18, "t_max": 34, "carbon": 4, "comm": "High - Flue-Cured Virginia Export Tobacco"},
    {"name": "Mysuru Mallige (Jasmine)", "type": "CROP", "zone": south_maidan, "drought": 6, "ph_min": 6.0, "ph_max": 7.5, "elev_min": 600, "elev_max": 900, "t_min": 20, "t_max": 35, "carbon": 4, "comm": "Very High - GI Tagged Fragrant Essential Flower"},
    {"name": "Hadagali Mallige", "type": "CROP", "zone": south_maidan, "drought": 7, "ph_min": 6.0, "ph_max": 7.5, "elev_min": 500, "elev_max": 850, "t_min": 20, "t_max": 36, "carbon": 4, "comm": "High - Star-Shaped High-Perfume Jasmine"},
    {"name": "Crossandra (Kanakambara)", "type": "CROP", "zone": south_maidan, "drought": 7, "ph_min": 6.0, "ph_max": 7.5, "elev_min": 600, "elev_max": 900, "t_min": 20, "t_max": 35, "carbon": 3, "comm": "High - Firecracker Flower Daily Temple Garland"},
    {"name": "Marigold (Pusa Narangi)", "type": "CROP", "zone": south_maidan, "drought": 7, "ph_min": 6.0, "ph_max": 7.5, "elev_min": 600, "elev_max": 1000, "t_min": 16, "t_max": 34, "carbon": 3, "comm": "High - Festival Garland & Lutein Dye Flower"},
    {"name": "Tomato (Arka Rakshak)", "type": "CROP", "zone": south_maidan, "drought": 6, "ph_min": 6.0, "ph_max": 7.5, "elev_min": 600, "elev_max": 1000, "t_min": 18, "t_max": 34, "carbon": 3, "comm": "High - Triple Disease Resistant Hybrid Tomato"},
    {"name": "Potato (Kufri Jyoti)", "type": "CROP", "zone": south_maidan, "drought": 5, "ph_min": 5.2, "ph_max": 6.8, "elev_min": 700, "elev_max": 1100, "t_min": 14, "t_max": 28, "carbon": 3, "comm": "High - Commercial Table Potato Tuber"},
    {"name": "Capsicum (Indra Green)", "type": "CROP", "zone": south_maidan, "drought": 5, "ph_min": 6.0, "ph_max": 7.0, "elev_min": 600, "elev_max": 1000, "t_min": 16, "t_max": 30, "carbon": 3, "comm": "High - Polyhouse & Open Field Sweet Pepper"},
    {"name": "Bangalore Blue Grapes", "type": "CROP", "zone": south_maidan, "drought": 7, "ph_min": 6.0, "ph_max": 7.5, "elev_min": 700, "elev_max": 950, "t_min": 15, "t_max": 32, "carbon": 5, "comm": "Very High - GI Tagged Juice & Wine Grape"},
    {"name": "Yelakki Banana", "type": "CROP", "zone": south_maidan, "drought": 5, "ph_min": 6.0, "ph_max": 7.5, "elev_min": 550, "elev_max": 900, "t_min": 20, "t_max": 35, "carbon": 6, "comm": "Very High - Premium Small Sweet Table Banana"},
    {"name": "Grand Naine Banana (G-9)", "type": "CROP", "zone": south_maidan, "drought": 5, "ph_min": 6.0, "ph_max": 7.5, "elev_min": 550, "elev_max": 900, "t_min": 20, "t_max": 35, "carbon": 6, "comm": "High - High-Volume Cavendish Banana"},
    {"name": "Papaya (Red Lady 786)", "type": "CROP", "zone": south_maidan, "drought": 6, "ph_min": 6.0, "ph_max": 7.5, "elev_min": 550, "elev_max": 900, "t_min": 20, "t_max": 36, "carbon": 5, "comm": "High - Red Sweet Flesh Table Papaya"},
    # Trees & Agroforestry
    {"name": "Mango (Alphonso / Badami)", "type": "TREE", "zone": south_maidan, "drought": 7, "ph_min": 5.5, "ph_max": 7.5, "elev_min": 500, "elev_max": 900, "t_min": 18, "t_max": 36, "carbon": 8, "comm": "Very High - King of Mangoes Export Grade"},
    {"name": "Mango (Totapuri / Banganapalli)", "type": "TREE", "zone": south_maidan, "drought": 8, "ph_min": 5.5, "ph_max": 7.5, "elev_min": 500, "elev_max": 900, "t_min": 18, "t_max": 38, "carbon": 8, "comm": "High - Commercial Pulp Processing Mango"},
    {"name": "Mango (Raspuri / Mallika)", "type": "TREE", "zone": south_maidan, "drought": 7, "ph_min": 5.5, "ph_max": 7.5, "elev_min": 500, "elev_max": 900, "t_min": 18, "t_max": 36, "carbon": 8, "comm": "High - Table Dessert Juicy Mango"},
    {"name": "Guava (Allahabad Safeda)", "type": "TREE", "zone": south_maidan, "drought": 8, "ph_min": 5.5, "ph_max": 7.8, "elev_min": 500, "elev_max": 950, "t_min": 18, "t_max": 36, "carbon": 7, "comm": "High - High Vitamin C Table Guava"},
    {"name": "Sapota (Kalipatti Chiku)", "type": "TREE", "zone": south_maidan, "drought": 8, "ph_min": 5.8, "ph_max": 7.8, "elev_min": 500, "elev_max": 900, "t_min": 18, "t_max": 36, "carbon": 8, "comm": "High - High Sweetness Commercial Chiku"},
    {"name": "Mulberry (Reshme V-1)", "type": "TREE", "zone": south_maidan, "drought": 7, "ph_min": 6.0, "ph_max": 7.5, "elev_min": 550, "elev_max": 950, "t_min": 18, "t_max": 35, "carbon": 7, "comm": "Very High - Mysore Silk Sericulture Foliage"},
    {"name": "Pongamia (Honge Mara)", "type": "TREE", "zone": south_maidan, "drought": 9, "ph_min": 5.5, "ph_max": 8.5, "elev_min": 400, "elev_max": 900, "t_min": 18, "t_max": 40, "carbon": 9, "comm": "High - Bio-Diesel Seed Oil & Green Manure"},
    {"name": "Moringa (Drumstick PKM-1)", "type": "TREE", "zone": south_maidan, "drought": 8, "ph_min": 6.0, "ph_max": 8.0, "elev_min": 400, "elev_max": 900, "t_min": 20, "t_max": 38, "carbon": 7, "comm": "High - Superfood Nutrition Pods & Leaves"},
    {"name": "Amla (Indian Gooseberry)", "type": "TREE", "zone": south_maidan, "drought": 8, "ph_min": 6.0, "ph_max": 8.2, "elev_min": 400, "elev_max": 950, "t_min": 16, "t_max": 38, "carbon": 7, "comm": "High - Ayurvedic Chyawanprash Vitamin C Fruit"},
    {"name": "Jamun (Black Plum)", "type": "TREE", "zone": south_maidan, "drought": 8, "ph_min": 5.5, "ph_max": 7.8, "elev_min": 400, "elev_max": 900, "t_min": 18, "t_max": 38, "carbon": 8, "comm": "High - Anti-Diabetic Fruit Pulp & Timber"},
    {"name": "Eucalyptus (Clonal Hybrid)", "type": "TREE", "zone": south_maidan, "drought": 8, "ph_min": 5.0, "ph_max": 8.0, "elev_min": 400, "elev_max": 1000, "t_min": 16, "t_max": 40, "carbon": 9, "comm": "High - Fast 5-Year Paper Pulp & Poles"}
]

created_count = 0
updated_count = 0

for item in SPECIES_DATA:
    obj, created = SpeciesConstraint.objects.update_or_create(
        name=item["name"],
        defaults={
            "type": item["type"],
            "target_zone": item["zone"],
            "drought_tolerance": item["drought"],
            "soil_ph_min": item["ph_min"],
            "soil_ph_max": item["ph_max"],
            "min_elevation_m": item["elev_min"],
            "max_elevation_m": item["elev_max"],
            "ideal_temp_min_c": item["t_min"],
            "ideal_temp_max_c": item["t_max"],
            "carbon_rating": item["carbon"],
            "commercial_value": item["comm"]
        }
    )
    if created:
        created_count += 1
    else:
        updated_count += 1

print(f"Species catalog population complete! Created: {created_count}, Updated: {updated_count}, Total Species in DB: {SpeciesConstraint.objects.count()}")
