from rivers.models import River, MonitoringStation, EcologicalIndicator, Measurement

# Створення річок
poltva = River.objects.create(name='Полтва', length_km=60.5, pollution_level=7.5, monitoring_date='2024-01-01')
dnister = River.objects.create(name='Дністер', length_km=1362, pollution_level=3.0, monitoring_date='2024-02-15')

# Створення станцій
station_lviv = MonitoringStation.objects.create(name='Станція Львів', location='Львів', river=poltva)

# Створення екологічних показників
EcologicalIndicator.objects.create(river=poltva, indicator_name='pH', value=6.8)
EcologicalIndicator.objects.create(river=dnister, indicator_name='Кисень', value=8.0)

# Створення вимірювань
Measurement.objects.create(river=poltva, station=station_lviv, parameter='Температура', value=15.5, measurement_date='2024-01-02')

