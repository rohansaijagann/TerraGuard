import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'terraguard.settings')
django.setup()

from decision_support.models import KarnatakaAgroZone, SpeciesConstraint

def run():
    print("Clearing old data...")
    SpeciesConstraint.objects.all().delete()
    KarnatakaAgroZone.objects.all().delete()
    
    print("Creating Agro Zones...")
    coastal = KarnatakaAgroZone.objects.create(name="Coastal (Karavali)", soil_profile="Lateritic", min_rainfall_mm=2500, max_rainfall_mm=4000, base_elevation_m=50)
    malnad = KarnatakaAgroZone.objects.create(name="Western Ghats (Malnad)", soil_profile="Forest Loam", min_rainfall_mm=1500, max_rainfall_mm=3000, base_elevation_m=900)
    n_maidan = KarnatakaAgroZone.objects.create(name="Northern Maidan", soil_profile="Black Cotton", min_rainfall_mm=400, max_rainfall_mm=800, base_elevation_m=500)
    s_maidan = KarnatakaAgroZone.objects.create(name="Southern Maidan", soil_profile="Red Loam", min_rainfall_mm=600, max_rainfall_mm=1000, base_elevation_m=800)

    print("Creating Species...")
    
    # === COASTAL SPECIES ===
    SpeciesConstraint.objects.create(
        name="Coconut", type="TREE", target_zone=coastal,
        drought_tolerance=4, soil_ph_min=5.2, soil_ph_max=8.0,
        min_elevation_m=0, max_elevation_m=600,
        carbon_rating=8, commercial_value="High ROI Cash Crop"
    )
    SpeciesConstraint.objects.create(
        name="Arecanut (Betel Nut)", type="TREE", target_zone=coastal,
        drought_tolerance=3, soil_ph_min=5.5, soil_ph_max=7.0,
        min_elevation_m=0, max_elevation_m=800,
        carbon_rating=6, commercial_value="Very High ROI Cash Crop"
    )
    SpeciesConstraint.objects.create(
        name="Cashew", type="TREE", target_zone=coastal,
        drought_tolerance=8, soil_ph_min=4.5, soil_ph_max=6.5,
        min_elevation_m=0, max_elevation_m=700,
        carbon_rating=7, commercial_value="High ROI Export Crop"
    )
    SpeciesConstraint.objects.create(
        name="Rubber", type="TREE", target_zone=coastal,
        drought_tolerance=3, soil_ph_min=4.5, soil_ph_max=6.0,
        min_elevation_m=0, max_elevation_m=500,
        carbon_rating=9, commercial_value="Long-term Cash Crop"
    )
    SpeciesConstraint.objects.create(
        name="Cocoa", type="CROP", target_zone=coastal,
        drought_tolerance=2, soil_ph_min=5.0, soil_ph_max=7.5,
        min_elevation_m=0, max_elevation_m=500,
        carbon_rating=5, commercial_value="High Value Intercrop"
    )
    SpeciesConstraint.objects.create(
        name="Paddy (Coastal)", type="CROP", target_zone=coastal,
        drought_tolerance=1, soil_ph_min=5.0, soil_ph_max=6.5,
        min_elevation_m=0, max_elevation_m=200,
        carbon_rating=3, commercial_value="Staple Food Crop"
    )
    SpeciesConstraint.objects.create(
        name="Vanilla", type="CROP", target_zone=coastal,
        drought_tolerance=2, soil_ph_min=5.5, soil_ph_max=7.0,
        min_elevation_m=0, max_elevation_m=600,
        carbon_rating=4, commercial_value="Extremely High ROI Cash Crop"
    )
    SpeciesConstraint.objects.create(
        name="Nutmeg", type="TREE", target_zone=coastal,
        drought_tolerance=2, soil_ph_min=5.5, soil_ph_max=6.5,
        min_elevation_m=0, max_elevation_m=600,
        carbon_rating=6, commercial_value="High Value Spice"
    )
    SpeciesConstraint.objects.create(
        name="Cinnamon", type="TREE", target_zone=coastal,
        drought_tolerance=3, soil_ph_min=4.5, soil_ph_max=5.5,
        min_elevation_m=0, max_elevation_m=500,
        carbon_rating=7, commercial_value="Commercial Spice"
    )
    SpeciesConstraint.objects.create(
        name="Pineapple", type="CROP", target_zone=coastal,
        drought_tolerance=6, soil_ph_min=4.5, soil_ph_max=6.0,
        min_elevation_m=0, max_elevation_m=800,
        carbon_rating=3, commercial_value="Commercial Fruit"
    )
    SpeciesConstraint.objects.create(
        name="Bamboo", type="TREE", target_zone=coastal,
        drought_tolerance=7, soil_ph_min=5.0, soil_ph_max=6.5,
        min_elevation_m=0, max_elevation_m=1000,
        carbon_rating=10, commercial_value="Sustainable Timber / Fast Growth"
    )

    # === MALNAD (WESTERN GHATS) SPECIES ===
    SpeciesConstraint.objects.create(
        name="Coffee (Arabica)", type="CROP", target_zone=malnad,
        drought_tolerance=4, soil_ph_min=5.0, soil_ph_max=6.0,
        min_elevation_m=1000, max_elevation_m=1500,
        carbon_rating=6, commercial_value="High ROI Export Crop"
    )
    SpeciesConstraint.objects.create(
        name="Coffee (Robusta)", type="CROP", target_zone=malnad,
        drought_tolerance=5, soil_ph_min=5.0, soil_ph_max=6.0,
        min_elevation_m=500, max_elevation_m=1000,
        carbon_rating=6, commercial_value="High ROI Export Crop"
    )
    SpeciesConstraint.objects.create(
        name="Black Pepper", type="CROP", target_zone=malnad,
        drought_tolerance=3, soil_ph_min=5.5, soil_ph_max=6.5,
        min_elevation_m=500, max_elevation_m=1500,
        carbon_rating=4, commercial_value="High Value Spice"
    )
    SpeciesConstraint.objects.create(
        name="Cardamom", type="CROP", target_zone=malnad,
        drought_tolerance=2, soil_ph_min=5.5, soil_ph_max=6.5,
        min_elevation_m=600, max_elevation_m=1500,
        carbon_rating=3, commercial_value="Very High ROI Spice"
    )
    SpeciesConstraint.objects.create(
        name="Silver Oak", type="TREE", target_zone=malnad,
        drought_tolerance=7, soil_ph_min=5.0, soil_ph_max=6.5,
        min_elevation_m=800, max_elevation_m=1500,
        carbon_rating=9, commercial_value="Timber & Coffee Shade Tree"
    )
    SpeciesConstraint.objects.create(
        name="Teak", type="TREE", target_zone=malnad,
        drought_tolerance=6, soil_ph_min=6.5, soil_ph_max=7.5,
        min_elevation_m=200, max_elevation_m=800,
        carbon_rating=8, commercial_value="Premium Timber"
    )
    SpeciesConstraint.objects.create(
        name="Rosewood", type="TREE", target_zone=malnad,
        drought_tolerance=5, soil_ph_min=5.5, soil_ph_max=7.0,
        min_elevation_m=500, max_elevation_m=1000,
        carbon_rating=10, commercial_value="Luxury Timber (Regulated)"
    )
    SpeciesConstraint.objects.create(
        name="Clove", type="TREE", target_zone=malnad,
        drought_tolerance=3, soil_ph_min=5.5, soil_ph_max=7.0,
        min_elevation_m=500, max_elevation_m=1000,
        carbon_rating=7, commercial_value="Premium Spice"
    )
    SpeciesConstraint.objects.create(
        name="Tea", type="CROP", target_zone=malnad,
        drought_tolerance=3, soil_ph_min=4.5, soil_ph_max=5.5,
        min_elevation_m=1200, max_elevation_m=2000,
        carbon_rating=5, commercial_value="High ROI Plantation Crop"
    )
    SpeciesConstraint.objects.create(
        name="Avocado", type="TREE", target_zone=malnad,
        drought_tolerance=4, soil_ph_min=6.0, soil_ph_max=7.0,
        min_elevation_m=800, max_elevation_m=1500,
        carbon_rating=6, commercial_value="Superfood Cash Crop"
    )
    SpeciesConstraint.objects.create(
        name="Garcinia (Murugal)", type="TREE", target_zone=malnad,
        drought_tolerance=4, soil_ph_min=5.5, soil_ph_max=6.5,
        min_elevation_m=200, max_elevation_m=800,
        carbon_rating=8, commercial_value="Medicinal & Culinary"
    )

    # === NORTHERN MAIDAN (ARID/SEMI-ARID) SPECIES ===
    SpeciesConstraint.objects.create(
        name="Jowar (Sorghum)", type="CROP", target_zone=n_maidan,
        drought_tolerance=9, soil_ph_min=6.0, soil_ph_max=8.5,
        min_elevation_m=300, max_elevation_m=900,
        carbon_rating=4, commercial_value="Drought-resistant Staple"
    )
    SpeciesConstraint.objects.create(
        name="Bajra (Pearl Millet)", type="CROP", target_zone=n_maidan,
        drought_tolerance=10, soil_ph_min=5.5, soil_ph_max=8.0,
        min_elevation_m=200, max_elevation_m=800,
        carbon_rating=3, commercial_value="Hardy Dryland Grain"
    )
    SpeciesConstraint.objects.create(
        name="Cotton", type="CROP", target_zone=n_maidan,
        drought_tolerance=7, soil_ph_min=5.5, soil_ph_max=8.5,
        min_elevation_m=300, max_elevation_m=800,
        carbon_rating=4, commercial_value="Major Cash Crop"
    )
    SpeciesConstraint.objects.create(
        name="Sunflower", type="CROP", target_zone=n_maidan,
        drought_tolerance=7, soil_ph_min=6.0, soil_ph_max=7.5,
        min_elevation_m=300, max_elevation_m=900,
        carbon_rating=4, commercial_value="Oilseed Cash Crop"
    )
    SpeciesConstraint.objects.create(
        name="Toor Dal (Pigeon Pea)", type="CROP", target_zone=n_maidan,
        drought_tolerance=8, soil_ph_min=5.5, soil_ph_max=7.5,
        min_elevation_m=300, max_elevation_m=800,
        carbon_rating=5, commercial_value="Protein-rich Pulse"
    )
    SpeciesConstraint.objects.create(
        name="Neem", type="TREE", target_zone=n_maidan,
        drought_tolerance=10, soil_ph_min=6.2, soil_ph_max=8.5,
        min_elevation_m=0, max_elevation_m=1000,
        carbon_rating=8, commercial_value="Medicinal / Timber"
    )
    SpeciesConstraint.objects.create(
        name="Tamarind", type="TREE", target_zone=n_maidan,
        drought_tolerance=9, soil_ph_min=5.5, soil_ph_max=8.5,
        min_elevation_m=0, max_elevation_m=1000,
        carbon_rating=7, commercial_value="Fruit & Shade Tree"
    )
    SpeciesConstraint.objects.create(
        name="Banyan", type="TREE", target_zone=n_maidan,
        drought_tolerance=9, soil_ph_min=5.0, soil_ph_max=8.0,
        min_elevation_m=0, max_elevation_m=1200,
        carbon_rating=10, commercial_value="Ecological / Shade"
    )
    SpeciesConstraint.objects.create(
        name="Wheat", type="CROP", target_zone=n_maidan,
        drought_tolerance=5, soil_ph_min=6.0, soil_ph_max=7.5,
        min_elevation_m=500, max_elevation_m=1000,
        carbon_rating=4, commercial_value="Winter Commercial Crop"
    )
    SpeciesConstraint.objects.create(
        name="Chickpea (Bengal Gram)", type="CROP", target_zone=n_maidan,
        drought_tolerance=7, soil_ph_min=6.0, soil_ph_max=8.0,
        min_elevation_m=400, max_elevation_m=900,
        carbon_rating=4, commercial_value="High Protein Cash Crop"
    )
    SpeciesConstraint.objects.create(
        name="Safflower", type="CROP", target_zone=n_maidan,
        drought_tolerance=9, soil_ph_min=6.0, soil_ph_max=8.0,
        min_elevation_m=400, max_elevation_m=900,
        carbon_rating=4, commercial_value="Oilseed (Drought Hardy)"
    )
    SpeciesConstraint.objects.create(
        name="Chilli (Byadgi)", type="CROP", target_zone=n_maidan,
        drought_tolerance=6, soil_ph_min=6.0, soil_ph_max=7.0,
        min_elevation_m=400, max_elevation_m=900,
        carbon_rating=4, commercial_value="Very High ROI Spice"
    )
    SpeciesConstraint.objects.create(
        name="Pomegranate", type="TREE", target_zone=n_maidan,
        drought_tolerance=8, soil_ph_min=5.5, soil_ph_max=7.5,
        min_elevation_m=500, max_elevation_m=1200,
        carbon_rating=5, commercial_value="High ROI Export Fruit"
    )
    SpeciesConstraint.objects.create(
        name="Fig", type="TREE", target_zone=n_maidan,
        drought_tolerance=8, soil_ph_min=6.0, soil_ph_max=8.0,
        min_elevation_m=500, max_elevation_m=1000,
        carbon_rating=6, commercial_value="Commercial Fruit"
    )
    SpeciesConstraint.objects.create(
        name="Acacia (Babul)", type="TREE", target_zone=n_maidan,
        drought_tolerance=10, soil_ph_min=5.5, soil_ph_max=8.5,
        min_elevation_m=200, max_elevation_m=800,
        carbon_rating=7, commercial_value="Timber & Ecological Restoration"
    )

    # === SOUTHERN MAIDAN SPECIES ===
    SpeciesConstraint.objects.create(
        name="Ragi (Finger Millet)", type="CROP", target_zone=s_maidan,
        drought_tolerance=8, soil_ph_min=5.0, soil_ph_max=8.0,
        min_elevation_m=600, max_elevation_m=1200,
        carbon_rating=4, commercial_value="Superfood Staple"
    )
    SpeciesConstraint.objects.create(
        name="Maize", type="CROP", target_zone=s_maidan,
        drought_tolerance=5, soil_ph_min=5.5, soil_ph_max=7.5,
        min_elevation_m=500, max_elevation_m=1200,
        carbon_rating=5, commercial_value="High Yield Feed/Food"
    )
    SpeciesConstraint.objects.create(
        name="Groundnut", type="CROP", target_zone=s_maidan,
        drought_tolerance=7, soil_ph_min=6.0, soil_ph_max=7.0,
        min_elevation_m=400, max_elevation_m=1000,
        carbon_rating=4, commercial_value="Oilseed / Snack"
    )
    SpeciesConstraint.objects.create(
        name="Mango", type="TREE", target_zone=s_maidan,
        drought_tolerance=7, soil_ph_min=5.5, soil_ph_max=7.5,
        min_elevation_m=0, max_elevation_m=1200,
        carbon_rating=8, commercial_value="High ROI Fruit"
    )
    SpeciesConstraint.objects.create(
        name="Sandalwood", type="TREE", target_zone=s_maidan,
        drought_tolerance=8, soil_ph_min=6.0, soil_ph_max=7.5,
        min_elevation_m=600, max_elevation_m=1200,
        carbon_rating=7, commercial_value="Ultra High ROI Timber"
    )
    SpeciesConstraint.objects.create(
        name="Jackfruit", type="TREE", target_zone=s_maidan,
        drought_tolerance=6, soil_ph_min=5.5, soil_ph_max=7.0,
        min_elevation_m=0, max_elevation_m=1500,
        carbon_rating=8, commercial_value="Fruit & Timber"
    )
    SpeciesConstraint.objects.create(
        name="Guava", type="TREE", target_zone=s_maidan,
        drought_tolerance=7, soil_ph_min=4.5, soil_ph_max=8.2,
        min_elevation_m=0, max_elevation_m=1500,
        carbon_rating=6, commercial_value="Commercial Fruit"
    )
    SpeciesConstraint.objects.create(
        name="Papaya", type="CROP", target_zone=s_maidan,
        drought_tolerance=4, soil_ph_min=5.5, soil_ph_max=7.0,
        min_elevation_m=0, max_elevation_m=1000,
        carbon_rating=4, commercial_value="Fast Cash Crop"
    )
    SpeciesConstraint.objects.create(
        name="Moringa (Drumstick)", type="TREE", target_zone=s_maidan,
        drought_tolerance=9, soil_ph_min=6.0, soil_ph_max=8.0,
        min_elevation_m=0, max_elevation_m=1000,
        carbon_rating=7, commercial_value="Superfood / Medicinal"
    )
    SpeciesConstraint.objects.create(
        name="Eucalyptus", type="TREE", target_zone=s_maidan,
        drought_tolerance=8, soil_ph_min=5.0, soil_ph_max=7.5,
        min_elevation_m=0, max_elevation_m=1500,
        carbon_rating=9, commercial_value="Pulpwood (Caution: Water Intensive)"
    )
    SpeciesConstraint.objects.create(
        name="Sugarcane", type="CROP", target_zone=s_maidan,
        drought_tolerance=2, soil_ph_min=6.0, soil_ph_max=7.5,
        min_elevation_m=0, max_elevation_m=1000,
        carbon_rating=6, commercial_value="Major Cash Crop (Irrigated)"
    )
    SpeciesConstraint.objects.create(
        name="Mulberry", type="TREE", target_zone=s_maidan,
        drought_tolerance=6, soil_ph_min=6.0, soil_ph_max=7.5,
        min_elevation_m=500, max_elevation_m=1000,
        carbon_rating=7, commercial_value="Sericulture Cash Crop"
    )
    SpeciesConstraint.objects.create(
        name="Grapes", type="CROP", target_zone=s_maidan,
        drought_tolerance=6, soil_ph_min=6.5, soil_ph_max=7.5,
        min_elevation_m=700, max_elevation_m=1000,
        carbon_rating=5, commercial_value="Vineyard Export Crop"
    )
    SpeciesConstraint.objects.create(
        name="Amla (Indian Gooseberry)", type="TREE", target_zone=s_maidan,
        drought_tolerance=8, soil_ph_min=6.0, soil_ph_max=8.0,
        min_elevation_m=0, max_elevation_m=1200,
        carbon_rating=7, commercial_value="Medicinal Superfood"
    )
    SpeciesConstraint.objects.create(
        name="Turmeric", type="CROP", target_zone=s_maidan,
        drought_tolerance=3, soil_ph_min=5.5, soil_ph_max=7.0,
        min_elevation_m=400, max_elevation_m=1000,
        carbon_rating=4, commercial_value="High Value Spice"
    )
    SpeciesConstraint.objects.create(
        name="Jasmine (Mysuru Mallige)", type="CROP", target_zone=s_maidan,
        drought_tolerance=5, soil_ph_min=6.0, soil_ph_max=7.0,
        min_elevation_m=600, max_elevation_m=900,
        carbon_rating=4, commercial_value="Premium Floriculture"
    )
    SpeciesConstraint.objects.create(
        name="Pongamia (Honge)", type="TREE", target_zone=s_maidan,
        drought_tolerance=9, soil_ph_min=5.5, soil_ph_max=8.5,
        min_elevation_m=0, max_elevation_m=1200,
        carbon_rating=9, commercial_value="Biofuel & Ecological"
    )
    SpeciesConstraint.objects.create(
        name="Tomato", type="CROP", target_zone=s_maidan,
        drought_tolerance=4, soil_ph_min=6.0, soil_ph_max=7.0,
        min_elevation_m=400, max_elevation_m=1000,
        carbon_rating=3, commercial_value="Daily Cash Crop"
    )

    print(f"Success! Inserted {SpeciesConstraint.objects.count()} species across {KarnatakaAgroZone.objects.count()} agro-zones.")

if __name__ == '__main__':
    run()
