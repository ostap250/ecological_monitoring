from django.shortcuts import render
from rest_framework import viewsets
from .models import River, MonitoringStation, EcologicalIndicator, Measurement
from .serializers import RiverSerializer, MonitoringStationSerializer, EcologicalIndicatorSerializer, MeasurementSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .fuzzy_logic import calculate_rating_and_recommendation
from rest_framework.exceptions import ValidationError
from django.http import JsonResponse
from django.views import View

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

# class FuzzyLogicView(View):
#     def get(self, request, *args, **kwargs):
#         return JsonResponse({"message": "GET method is allowed and working!"})

#     def post(self, request, *args, **kwargs):
#         return JsonResponse({"message": "POST method is allowed and working!"})
    
class FuzzyLogicView(APIView):
    
    def get(self, request, *args, **kwargs):
        # Повернення повідомлення для перевірки
        return Response({"message": "GET method is allowed and working!"})
    
    def post(self, request):
        data = request.data

        # Валідація вхідних даних
        try:
            oxygen = float(data.get('oxygen', 50))
            biological_index = float(data.get('biological_index', 50))
            pollutant_concentration = float(data.get('pollutant_concentration', 50))

            # Перевірка діапазонів
            if not (0 <= oxygen <= 15):
                raise ValidationError("Oxygen level must be between 0 and 15.")
            if not (0 <= biological_index <= 10):
                raise ValidationError("Biological index must be between 0 and 10.")
            if not (0 <= pollutant_concentration <= 100):
                raise ValidationError("Pollutant concentration must be between 0 and 100.")
        except (ValueError, TypeError):
            raise ValidationError("Invalid input data. Please provide numeric values.")

        # Обчислення рейтингу та рекомендацій
        rating, recommendation = calculate_rating_and_recommendation(
            oxygen, biological_index, pollutant_concentration
        )
    

        return Response({
            'rating': rating,
            'recommendation': recommendation
        })