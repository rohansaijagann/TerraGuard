from django.contrib import admin
from .models import KarnatakaAgroZone, SpeciesConstraint

@admin.register(KarnatakaAgroZone)
class KarnatakaAgroZoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'min_rainfall_mm', 'max_rainfall_mm', 'base_elevation_m')

@admin.register(SpeciesConstraint)
class SpeciesConstraintAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'target_zone', 'drought_tolerance')
    list_filter = ('type', 'target_zone')