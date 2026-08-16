from django.urls import path
from .views import RecommendationAPI, DiagnosticsAPI, FireRiskAPI, ForestBoundariesAPI, DroughtScanAPI, FireScanAPI, PestDiseaseAPI, LiveAlertsAPI, dashboard_view

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
]