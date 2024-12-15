from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin 
from .views import process_river_data  # Імпортуйте вашу функцію з views.py
from .views import (
    RiverViewSet, 
    MonitoringStationViewSet, 
    EcologicalIndicatorViewSet, 
    MeasurementViewSet, 
    FuzzyLogicView,
    process_river_data  # Додана функція
)

# Створення маршрутизатора
router = DefaultRouter()
router.register('rivers', RiverViewSet, basename='river')
router.register('monitoring-stations', MonitoringStationViewSet, basename='monitoringstation')
router.register('ecological-indicators', EcologicalIndicatorViewSet, basename='ecologicalindicator')
router.register('measurements', MeasurementViewSet, basename='measurement')

# Визначення URL
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rivers.urls')), # Додайте ваші шляхи для застосунку rivers
    path('', include(router.urls)),  # Додає маршрути з маршрутизатора
    path('fuzzy-logic/', FuzzyLogicView.as_view(), name='fuzzy_logic'),  # Окремий маршрут для нечіткої логіки
    path('api/process-data/', process_river_data, name='process_data'),  # Маршрут для обробки даних
    path('process/', process_river_data, name='process_river_data'),
]
