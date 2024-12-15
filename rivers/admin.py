from django.contrib import admin
from .models import River, MonitoringStation, EcologicalIndicator, Measurement
from .models import SensorData


admin.site.register(SensorData)
admin.site.register(River)
admin.site.register(MonitoringStation)
admin.site.register(EcologicalIndicator)
admin.site.register(Measurement)
