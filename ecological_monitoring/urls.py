"""ecological_monitoring URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.http import JsonResponse
from django.contrib import admin
from django.urls import path, include
from rivers.views import FuzzyLogicView  # Імпорт вашого View для нечіткої логіки
from rest_framework.routers import DefaultRouter
from rivers.views import RiverViewSet, MonitoringStationViewSet, EcologicalIndicatorViewSet, MeasurementViewSet

router = DefaultRouter()
router.register(r'rivers', RiverViewSet)
router.register(r'stations', MonitoringStationViewSet)
router.register(r'indicators', EcologicalIndicatorViewSet)
router.register(r'measurements', MeasurementViewSet)

urlpatterns = [
    path('', lambda request: JsonResponse({"message": "Site is working for now"})),  # Кореневий маршрут
    path('admin/', admin.site.urls),  # Адмін-панель
    path('api/', include(router.urls)),  # REST-маршрути
    path('api/fuzzy-logic/', FuzzyLogicView.as_view(), name='fuzzy_logic'),  # Нечітка логіка
]


