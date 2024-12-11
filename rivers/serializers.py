from rest_framework import serializers
from .models import River, MonitoringStation, EcologicalIndicator, Measurement

class RiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = River
        fields = '__all__'

class MonitoringStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringStation
        fields = '__all__'

class EcologicalIndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EcologicalIndicator
        fields = '__all__'

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'
