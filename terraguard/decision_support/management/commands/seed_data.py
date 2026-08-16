from django.core.management.base import BaseCommand
from decision_support.models import KarnatakaAgroZone, SpeciesConstraint

class Command(BaseCommand):
    help = 'Seeds the database with a production-scale TerraGuard botanical dataset'

    def handle(self, *args, **kwargs):
        self.stdout.write('Purging old database records...')
        SpeciesConstraint.objects.all().delete()
        KarnatakaAgroZone.objects.all().delete()

        # 1. Initialize Zones
        zones = {
            "Western Ghats": KarnatakaAgroZone.objects.create(name="Western Ghats", soil_profile="Laterite", min_rainfall_mm=2000, max_rainfall_mm=4500, base_elevation_m=600),
            "Southern Maidan": KarnatakaAgroZone.objects.create(name="Southern Maidan", soil_profile="Red Loamy", min_rainfall_mm=600, max_rainfall_mm=1000, base_elevation_m=800),
            "Northern Maidan": KarnatakaAgroZone.objects.create(name="Northern Maidan", soil_profile="Black Cotton", min_rainfall_mm=300, max_rainfall_mm=700, base_elevation_m=400)
        }

        # 2. Production Dataset (Easily expandable to 100+ species)
        botanical_catalog = [
            # --- WESTERN GHATS (High Rainfall, High Elevation, Laterite Soil) ---
            {"name": "Teak", "type": "TREE", "zone": "Western Ghats", "dr": 4, "ph_min": 6.0, "ph_max": 7.5, "e_min": 0, "e_max": 1200, "c": 8, "val": "Premium high-value timber for luxury furniture and construction."},
            {"name": "Rosewood", "type": "TREE", "zone": "Western Ghats", "dr": 4, "ph_min": 5.5, "ph_max": 7.0, "e_min": 500, "e_max": 1500, "c": 7, "val": "Extremely high-value export timber, excellent carbon sink."},
            {"name": "Coffee (Arabica)", "type": "CROP", "zone": "Western Ghats", "dr": 2, "ph_min": 5.0, "ph_max": 6.5, "e_min": 1000, "e_max": 1500, "c": 3, "val": "Premium export cash crop, requires significant shade canopy."},
            {"name": "Coffee (Robusta)", "type": "CROP", "zone": "Western Ghats", "dr": 3, "ph_min": 5.0, "ph_max": 6.5, "e_min": 500, "e_max": 1000, "c": 4, "val": "High-yield cash crop, higher disease resistance than Arabica."},
            {"name": "Black Pepper", "type": "CROP", "zone": "Western Ghats", "dr": 2, "ph_min": 5.5, "ph_max": 6.5, "e_min": 0, "e_max": 1200, "c": 2, "val": "High-value spice creeper, intercropped with Silver Oak or Arecanut."},
            {"name": "Cardamom", "type": "CROP", "zone": "Western Ghats", "dr": 1, "ph_min": 4.5, "ph_max": 6.0, "e_min": 600, "e_max": 1500, "c": 3, "val": "Premium luxury spice, highly sensitive to drought."},
            {"name": "Arecanut", "type": "TREE", "zone": "Western Ghats", "dr": 3, "ph_min": 5.0, "ph_max": 7.0, "e_min": 0, "e_max": 1000, "c": 5, "val": "High-demand commercial palm, excellent for multi-tier cropping."},
            {"name": "Rubber", "type": "TREE", "zone": "Western Ghats", "dr": 3, "ph_min": 4.5, "ph_max": 6.0, "e_min": 0, "e_max": 500, "c": 6, "val": "Industrial latex production, highly lucrative in coastal/ghat transitions."},
            {"name": "Silver Oak", "type": "TREE", "zone": "Western Ghats", "dr": 5, "ph_min": 5.5, "ph_max": 7.5, "e_min": 500, "e_max": 1800, "c": 6, "val": "Primary shade tree for coffee estates, decent timber value."},
            {"name": "Jackfruit", "type": "TREE", "zone": "Western Ghats", "dr": 5, "ph_min": 5.5, "ph_max": 7.0, "e_min": 0, "e_max": 1200, "c": 5, "val": "Food security, timber, and drought-resistant fruit production."},
            {"name": "Mahogany", "type": "TREE", "zone": "Western Ghats", "dr": 4, "ph_min": 5.5, "ph_max": 7.5, "e_min": 100, "e_max": 1000, "c": 9, "val": "Luxury furniture timber, massive canopy for carbon offset."},
            {"name": "Cocoa", "type": "CROP", "zone": "Western Ghats", "dr": 2, "ph_min": 5.0, "ph_max": 7.0, "e_min": 0, "e_max": 800, "c": 3, "val": "High-value chocolate industry raw material, shade-dependent."},

            # --- SOUTHERN MAIDAN (Moderate Rainfall, Red Loamy Soil, Mod Elevation) ---
            {"name": "Sandalwood", "type": "TREE", "zone": "Southern Maidan", "dr": 7, "ph_min": 6.0, "ph_max": 7.5, "e_min": 600, "e_max": 1200, "c": 5, "val": "Ultra-luxury aromatic wood and essential oils. Highly regulated."},
            {"name": "Mango (Alphonso/Badami)", "type": "TREE", "zone": "Southern Maidan", "dr": 6, "ph_min": 5.5, "ph_max": 7.5, "e_min": 0, "e_max": 900, "c": 6, "val": "High domestic and export market demand fruit."},
            {"name": "Finger Millet (Ragi)", "type": "CROP", "zone": "Southern Maidan", "dr": 8, "ph_min": 5.5, "ph_max": 8.0, "e_min": 500, "e_max": 2000, "c": 2, "val": "Crucial staple food security, excellent drought resistance."},
            {"name": "Mulberry", "type": "CROP", "zone": "Southern Maidan", "dr": 6, "ph_min": 6.5, "ph_max": 7.5, "e_min": 300, "e_max": 900, "c": 4, "val": "Essential for sericulture (silk production), major rural income."},
            {"name": "Bamboo (Bambusa bambos)", "type": "TREE", "zone": "Southern Maidan", "dr": 6, "ph_min": 5.0, "ph_max": 8.0, "e_min": 0, "e_max": 1500, "c": 10, "val": "Rapid growth, construction material, supreme carbon credits."},
            {"name": "Tamarind", "type": "TREE", "zone": "Southern Maidan", "dr": 9, "ph_min": 5.5, "ph_max": 8.0, "e_min": 0, "e_max": 1000, "c": 7, "val": "High drought tolerance, culinary commercial value, deep roots."},
            {"name": "Coconut", "type": "TREE", "zone": "Southern Maidan", "dr": 5, "ph_min": 5.2, "ph_max": 8.0, "e_min": 0, "e_max": 600, "c": 6, "val": "Versatile cash crop (oil, coir, water)."},
            {"name": "Red Gram (Tur Dal)", "type": "CROP", "zone": "Southern Maidan", "dr": 7, "ph_min": 6.0, "ph_max": 7.5, "e_min": 200, "e_max": 1000, "c": 3, "val": "Primary protein staple, nitrogen-fixing legume."},
            {"name": "Moringa (Drumstick)", "type": "TREE", "zone": "Southern Maidan", "dr": 9, "ph_min": 6.0, "ph_max": 7.5, "e_min": 0, "e_max": 1200, "c": 5, "val": "Superfood export market, medicinal properties, fast-growing."},
            {"name": "Guava", "type": "TREE", "zone": "Southern Maidan", "dr": 7, "ph_min": 5.0, "ph_max": 8.0, "e_min": 0, "e_max": 1500, "c": 4, "val": "Hardy fruit tree, highly profitable with low maintenance."},
            {"name": "Sapota (Chikoo)", "type": "TREE", "zone": "Southern Maidan", "dr": 6, "ph_min": 6.0, "ph_max": 8.0, "e_min": 0, "e_max": 1000, "c": 5, "val": "Steady commercial fruit yield, wind-resistant."},

            # --- NORTHERN MAIDAN (Low Rainfall, Black Cotton Soil, Extreme Heat) ---
            {"name": "Neem", "type": "TREE", "zone": "Northern Maidan", "dr": 10, "ph_min": 6.2, "ph_max": 8.5, "e_min": 0, "e_max": 800, "c": 7, "val": "Biopesticide production, extreme drought survival, soil restoration."},
            {"name": "Sorghum (Jowar)", "type": "CROP", "zone": "Northern Maidan", "dr": 9, "ph_min": 6.0, "ph_max": 8.5, "e_min": 200, "e_max": 900, "c": 2, "val": "Vital dryland cereal and primary livestock fodder."},
            {"name": "Pomegranate", "type": "TREE", "zone": "Northern Maidan", "dr": 8, "ph_min": 6.5, "ph_max": 8.0, "e_min": 300, "e_max": 1200, "c": 4, "val": "High-value export fruit, excels in arid regions with drip irrigation."},
            {"name": "Acacia (Babul)", "type": "TREE", "zone": "Northern Maidan", "dr": 10, "ph_min": 5.5, "ph_max": 8.5, "e_min": 0, "e_max": 1000, "c": 8, "val": "Nitrogen-fixing, halts soil erosion, yields commercial gum."},
            {"name": "Cotton", "type": "CROP", "zone": "Northern Maidan", "dr": 7, "ph_min": 5.8, "ph_max": 8.0, "e_min": 100, "e_max": 800, "c": 3, "val": "Major commercial cash crop for the textile industry."},
            {"name": "Sunflower", "type": "CROP", "zone": "Northern Maidan", "dr": 8, "ph_min": 6.0, "ph_max": 7.5, "e_min": 200, "e_max": 900, "c": 2, "val": "Commercial edible oil extraction, thrives in black soil."},
            {"name": "Chickpea (Bengal Gram)", "type": "CROP", "zone": "Northern Maidan", "dr": 8, "ph_min": 6.0, "ph_max": 8.0, "e_min": 200, "e_max": 800, "c": 2, "val": "Winter legume crop, vital protein source, low water footprint."},
            {"name": "Fig (Anjeer)", "type": "TREE", "zone": "Northern Maidan", "dr": 9, "ph_min": 6.0, "ph_max": 8.0, "e_min": 300, "e_max": 1000, "c": 4, "val": "Drought-hardy fruit, high commercial value when dried."},
            {"name": "Indian Jujube (Ber)", "type": "TREE", "zone": "Northern Maidan", "dr": 10, "ph_min": 5.5, "ph_max": 8.5, "e_min": 0, "e_max": 1000, "c": 5, "val": "Extremely rugged, survives severe droughts, marketable fruit."},
            {"name": "Safflower", "type": "CROP", "zone": "Northern Maidan", "dr": 9, "ph_min": 6.5, "ph_max": 8.0, "e_min": 300, "e_max": 900, "c": 2, "val": "Deep-rooted oilseed crop, extracts moisture from deep soil layers."},
            {"name": "Aloe Vera", "type": "CROP", "zone": "Northern Maidan", "dr": 10, "ph_min": 7.0, "ph_max": 8.5, "e_min": 0, "e_max": 900, "c": 1, "val": "Pharmaceutical and cosmetic industry demand, needs minimal water."}
        ]

        self.stdout.write(f'Injecting {len(botanical_catalog)} botanical profiles...')

        # 3. Automated Injection Loop
        for item in botanical_catalog:
            SpeciesConstraint.objects.create(
                name=item["name"],
                type=item["type"],
                target_zone=zones[item["zone"]],
                drought_tolerance=item["dr"],
                soil_ph_min=item["ph_min"],
                soil_ph_max=item["ph_max"],
                min_elevation_m=item["e_min"],
                max_elevation_m=item["e_max"],
                carbon_rating=item["c"],
                commercial_value=item["val"]
            )

        self.stdout.write(self.style.SUCCESS('Successfully loaded production dataset!'))