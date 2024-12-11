from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RiverViewSet, MonitoringStationViewSet, EcologicalIndicatorViewSet, MeasurementViewSet
from .views import FuzzyLogicView
from django.urls import path

router = DefaultRouter()
router.register('rivers', RiverViewSet, basename='river')
router.register('monitoring-stations', MonitoringStationViewSet, basename='monitoringstation')
router.register('ecological-indicators', EcologicalIndicatorViewSet, basename='ecologicalindicator')
router.register('measurements', MeasurementViewSet, basename='measurement')

urlpatterns = [
    path('api/', include('rivers.urls')),  # Підключення маршрутів додатку rivers
    path('', include(router.urls)),
]
