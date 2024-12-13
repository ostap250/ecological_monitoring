from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RiverViewSet, MonitoringStationViewSet, EcologicalIndicatorViewSet, MeasurementViewSet, FuzzyLogicView

# Створення маршрутизатора
router = DefaultRouter()
router.register('rivers', RiverViewSet, basename='river')
router.register('monitoring-stations', MonitoringStationViewSet, basename='monitoringstation')
router.register('ecological-indicators', EcologicalIndicatorViewSet, basename='ecologicalindicator')
router.register('measurements', MeasurementViewSet, basename='measurement')

# Визначення URL
urlpatterns = [
    path('', include(router.urls)),  # Додає маршрути з маршрутизатора
    path('fuzzy-logic/', FuzzyLogicView.as_view(), name='fuzzy_logic'),  # Окремий маршрут для нечіткої логіки
]
