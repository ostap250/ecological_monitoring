from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WaterBodyViewSet, WaterQualityReportViewSet, ReportFileViewSet, WaterQualityViewSet

# Створюємо маршрутизатор для API
router = DefaultRouter()
router.register(r'water-bodies', WaterBodyViewSet, basename='waterbody')
router.register(r'water-quality-reports', WaterQualityReportViewSet, basename='waterqualityreport')
router.register(r'report-files', ReportFileViewSet, basename='reportfile')
router.register(r'water-quality', WaterQualityViewSet, basename='water_quality')

urlpatterns = [
    path('', include(router.urls)),
]