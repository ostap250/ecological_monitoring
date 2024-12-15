from django.db import models

class River(models.Model):
    name = models.CharField(max_length=255)
    length_km = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pollution_level = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    monitoring_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class MonitoringStation(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    river = models.ForeignKey(River, on_delete=models.CASCADE, related_name='stations')

    def __str__(self):
        return self.name

class SensorData(models.Model):
    oxygen = models.FloatField()
    biological_index = models.FloatField()
    pollutant_concentration = models.FloatField()
    temperature = models.FloatField()
    turbidity = models.FloatField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"Sensor Data at {self.timestamp}"


class EcologicalIndicator(models.Model):
    river = models.ForeignKey(River, on_delete=models.CASCADE, related_name='indicators')
    indicator_name = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.indicator_name

class Measurement(models.Model):
    river = models.ForeignKey(River, on_delete=models.CASCADE, related_name='measurements')
    station = models.ForeignKey(MonitoringStation, on_delete=models.CASCADE, related_name='measurements')
    parameter = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    measurement_date = models.DateField()

    def __str__(self):
        return f"{self.parameter} - {self.value}"
