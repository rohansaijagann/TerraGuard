from django.urls import path
from .views import (
    RecommendationAPI, DiagnosticsAPI, FireRiskAPI, ForestBoundariesAPI, 
    DroughtScanAPI, FireScanAPI, PestDiseaseAPI, LiveAlertsAPI, 
    YieldEstimatorAPI, ThermalHotspotsAPI,
    FertilizerCalcAPI, AgriPVModelerAPI, APMCMarketAPI, 
    CarbonCreditAPI, MachineryRentalAPI, PMFBYInsuranceAPI,
    RaithaSahayakaAPI,
    dashboard_view
)

urlpatterns = [
    path('', dashboard_view, name='dashboard'), 
    path('api/recommend/', RecommendationAPI.as_view(), name='api_recommend'),
    path('api/diagnostics/', DiagnosticsAPI.as_view(), name='api_diagnostics'),
    path('api/fire-risk/', FireRiskAPI.as_view(), name='api_fire_risk'),
    path('api/forest-boundaries/', ForestBoundariesAPI.as_view(), name='api_forest_boundaries'),
    path('api/drought-scan/', DroughtScanAPI.as_view(), name='api_drought_scan'),
    path('api/fire-scan/', FireScanAPI.as_view(), name='api_fire_scan'),
    path('api/pest-disease/', PestDiseaseAPI.as_view(), name='api_pest_disease'),
    path('api/live-alerts/', LiveAlertsAPI.as_view(), name='api_live_alerts'),
    path('api/estimate-yield/', YieldEstimatorAPI.as_view(), name='api_estimate_yield'),
    path('api/thermal-hotspots/', ThermalHotspotsAPI.as_view(), name='api_thermal_hotspots'),
    path('api/fertilizer-calc/', FertilizerCalcAPI.as_view(), name='api_fertilizer_calc'),
    path('api/agri-pv/', AgriPVModelerAPI.as_view(), name='api_agri_pv'),
    path('api/apmc-prices/', APMCMarketAPI.as_view(), name='api_apmc_prices'),
    path('api/carbon-credits/', CarbonCreditAPI.as_view(), name='api_carbon_credits'),
    path('api/machinery-rental/', MachineryRentalAPI.as_view(), name='api_machinery_rental'),
    path('api/pmfby-insurance/', PMFBYInsuranceAPI.as_view(), name='api_pmfby_insurance'),
    path('api/raitha-sahayaka/', RaithaSahayakaAPI.as_view(), name='api_raitha_sahayaka'),
]