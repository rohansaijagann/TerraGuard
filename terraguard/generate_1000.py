import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'terraguard.settings')
django.setup()

from decision_support.models import KarnatakaAgroZone, SpeciesConstraint

def run():
    print("Generating 1000+ species variants...")
    
    # Get all existing base species
    base_species = list(SpeciesConstraint.objects.all())
    
    if not base_species:
        print("No base species found! Run populate_db.py first.")
        return
        
    print(f"Found {len(base_species)} base species. Generating variants...")
    
    prefixes = ["High-Yield", "Drought-Resistant", "Coastal", "Hybrid", "Native", "Commercial", "Premium", "Dwarf", "Fast-Growing", "Organic"]
    suffixes = ["V1", "V2", "Pro", "Max", "Estate", "Select", "Plus", "Ultra", "Alpha", "Beta"]
    
    new_species_list = []
    
    # Generate ~20 variants per base species to reach >1000
    for base in base_species:
        for i in range(20):
            prefix = random.choice(prefixes)
            suffix = random.choice(suffixes)
            
            # Clean base name (remove existing parentheses if any)
            clean_name = base.name.split('(')[0].strip()
            variant_name = f"{clean_name} ({prefix} {suffix})"
            
            # Slight random variations in parameters to make them unique
            rain_min = max(0, base.target_zone.min_rainfall_mm * random.uniform(0.8, 1.2))
            elev_min = max(0, base.min_elevation_m + random.randint(-100, 100))
            elev_max = base.max_elevation_m + random.randint(-200, 200)
            
            ph_min = max(1.0, base.soil_ph_min + random.uniform(-0.5, 0.5))
            ph_max = min(14.0, base.soil_ph_max + random.uniform(-0.5, 0.5))
            if ph_min > ph_max:
                ph_min, ph_max = ph_max, ph_min
                
            drought = max(1, min(10, base.drought_tolerance + random.randint(-2, 2)))
            carbon = max(1, min(10, base.carbon_rating + random.randint(-1, 1)))
            
            new_species = SpeciesConstraint(
                name=variant_name,
                type=base.type,
                target_zone=base.target_zone,
                drought_tolerance=drought,
                soil_ph_min=round(ph_min, 1),
                soil_ph_max=round(ph_max, 1),
                min_elevation_m=int(elev_min),
                max_elevation_m=int(elev_max),
                carbon_rating=carbon,
                commercial_value=base.commercial_value
            )
            new_species_list.append(new_species)
            
    print(f"Bulk inserting {len(new_species_list)} new varieties...")
    SpeciesConstraint.objects.bulk_create(new_species_list)
    
    total = SpeciesConstraint.objects.count()
    print(f"Success! Database now contains {total} total species and varieties.")

if __name__ == '__main__':
    run()
