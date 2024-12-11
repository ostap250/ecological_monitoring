from django.shortcuts import render
from rest_framework import viewsets
from .models import River, MonitoringStation, EcologicalIndicator, Measurement
from .serializers import RiverSerializer, MonitoringStationSerializer, EcologicalIndicatorSerializer, MeasurementSerializer
from .fuzzy_logic import calculate_rating_and_recommendation
from rest_framework.views import APIView
from rest_framework.response import Response
from .fuzzy_logic import calculate_rating_and_recommendation

class RiverViewSet(viewsets.ModelViewSet):
    queryset = River.objects.all()
    serializer_class = RiverSerializer

class MonitoringStationViewSet(viewsets.ModelViewSet):
    queryset = MonitoringStation.objects.all()
    serializer_class = MonitoringStationSerializer

class EcologicalIndicatorViewSet(viewsets.ModelViewSet):
    queryset = EcologicalIndicator.objects.all()
    serializer_class = EcologicalIndicatorSerializer

class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

class FuzzyLogicView(APIView):
    def post(self, request):
        data = request.data
        # Отримання даних для нечіткої логіки
        water_quality = data.get('water_quality', 50)
        biodiversity = data.get('biodiversity', 50)
        pollution = data.get('pollution', 50)
        human_activity = data.get('human_activity', 50)

        # Виклик функції для обчислення
        rating, recommendation = calculate_rating_and_recommendation(water_quality, biodiversity, pollution, human_activity)

        # Відповідь з результатами
        return Response({
            'rating': rating,
            'recommendation': recommendation
        })
