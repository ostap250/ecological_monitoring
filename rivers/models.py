from django.db import models

class WaterBody(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Назва водойми")
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Довгота")
    description = models.TextField(null=True, blank=True, verbose_name="Опис")

    def __str__(self):
        return self.name

class WaterQualityReport(models.Model):
    water_body = models.ForeignKey(WaterBody, on_delete=models.CASCADE, related_name="quality_reports")
    date = models.DateField(verbose_name="Дата звіту")
    pollution_level = models.FloatField(verbose_name="Рівень забруднення")
    ph_level = models.FloatField(verbose_name="pH рівень")
    temperature = models.FloatField(verbose_name="Температура (°C)")

    def __str__(self):
        return f"Звіт {self.date} для {self.water_body.name}"

class ReportFile(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва звіту")
    file = models.FileField(upload_to="reports/", verbose_name="Файл звіту")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата завантаження")

    def __str__(self):
        return self.title
