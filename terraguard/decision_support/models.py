from django.db import models

class KarnatakaAgroZone(models.Model):
    name = models.CharField(max_length=100)
    soil_profile = models.CharField(max_length=100)
    min_rainfall_mm = models.IntegerField()
    max_rainfall_mm = models.IntegerField()
    base_elevation_m = models.IntegerField()

    def __str__(self):
        return self.name

class SpeciesConstraint(models.Model):
    TYPE_CHOICES = [('TREE', 'Tree'), ('CROP', 'Crop')]
    
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=4, choices=TYPE_CHOICES)
    target_zone = models.ForeignKey(KarnatakaAgroZone, on_delete=models.CASCADE)
    
    # Expanded Ecological Parameters
    drought_tolerance = models.IntegerField(help_text="Scale 1-10")
    soil_ph_min = models.FloatField()
    soil_ph_max = models.FloatField()
    
    # NEW: Deeper Analysis Parameters
    min_elevation_m = models.IntegerField(default=0)
    max_elevation_m = models.IntegerField(default=3000)
    ideal_temp_min_c = models.FloatField(default=15.0)
    ideal_temp_max_c = models.FloatField(default=35.0)
    carbon_rating = models.IntegerField(default=5, help_text="Scale 1-10 for CO2 absorption")
    
    commercial_value = models.TextField()

    def __str__(self):
        return self.name