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
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from .sensor_data_generator import generate_sensor_data, save_to_json_file
# ViewSets
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

# Fuzzy Logic API
class FuzzyLogicView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"message": "GET method is allowed and working!"})
    
    def post(self, request):
        data = request.data

        try:
            oxygen = float(data.get('oxygen', 50))
            biological_index = float(data.get('biological_index', 50))
            pollutant_concentration = float(data.get('pollutant_concentration', 50))
            temperature = float(data.get('temperature', 20))
            turbidity = float(data.get('turbidity', 30))

            print(f"Received values: oxygen={oxygen}, bio_index={biological_index}, "
              f"pollutant={pollutant_concentration}, temp={temperature}, turbidity={turbidity}")

            if not (0 <= oxygen <= 15):
                raise ValidationError("Oxygen level must be between 0 and 15.")
            if not (0 <= biological_index <= 10):
                raise ValidationError("Biological index must be between 0 and 10.")
            if not (0 <= pollutant_concentration <= 100):
                raise ValidationError("Pollutant concentration must be between 0 and 100.")
            if not (0 <= temperature <= 30):
                raise ValidationError("Temperature must be between 0 and 30 degrees Celsius.")
            if not (0 <= turbidity <= 100):
                raise ValidationError("Turbidity must be between 0 and 100 NTU.")
        except (ValueError, TypeError):
            raise ValidationError("Invalid input data. Please provide numeric values.")

        rating, recommendation = calculate_rating_and_recommendation(
            oxygen, biological_index, pollutant_concentration, temperature, turbidity
        )

        return Response({
            'rating': round(rating, 2),
            'recommendation': recommendation
        
        })
    
def sensor_data_view(request):
    """Імітація сенсора: генерація нових даних."""
    data = generate_sensor_data()
    save_to_json_file(data)  # Опціонально зберігаємо дані у файл
    return JsonResponse(data)

def process_river_data(request):
    # Ваш код для обробки даних річки тут
    return render(request, 'template_name.html', {})

# Клас для обробки даних з файлу data.json
@method_decorator(csrf_exempt, name='dispatch')
class ProcessRiverDataView(View):
    def post(self, request):
        try:
            # Читаємо дані з JSON-файлу
            with open('data.json', 'r', encoding='utf-8') as file:
                river_data = json.load(file)

            # Обробка даних через calculate_rating_and_recommendation
            results = []
            for river in river_data:
                rating, recommendation = calculate_rating_and_recommendation(
                    river['oxygen'],
                    river['biological_index'],
                    river['pollutant_concentration']
                )
                results.append({
                    "river": river['river'],
                    "rating": round(rating, 2),
                    "recommendation": recommendation
                })

            return JsonResponse({"results": results}, safe=False)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        
