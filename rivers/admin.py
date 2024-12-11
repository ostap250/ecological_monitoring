from django.contrib import admin
from .models import River, MonitoringStation, EcologicalIndicator, Measurement

admin.site.register(River)
admin.site.register(MonitoringStation)
admin.site.register(EcologicalIndicator)
admin.site.register(Measurement)
