from django.contrib import admin
from .models import WaterBody, WaterQualityReport, ReportFile


admin.site.register(WaterQualityReport)
admin.site.register(WaterBody)
admin.site.register(ReportFile)
