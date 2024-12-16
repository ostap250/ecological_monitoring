from rest_framework import serializers
from .models import WaterBody, WaterQualityReport, ReportFile

class WaterBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterBody
        fields = ['id', 'name', 'latitude', 'longitude', 'description']

class WaterQualityReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterQualityReport
        fields = ['id', 'water_body', 'date', 'pollution_level', 'ph_level', 'temperature']

class ReportFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportFile
        fields = ['id', 'title', 'file', 'uploaded_at']
