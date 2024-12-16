import random
from django.core.management.base import BaseCommand
from rivers.models import WaterBody, WaterQualityReport

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        # Create sample water bodies
        water_bodies = [
            {"name": "Дніпро", "latitude": 48.4647, "longitude": 35.0462, "description": "Найбільша річка України."},
            {"name": "Дністер", "latitude": 48.6235, "longitude": 25.6536, "description": "Важлива річка в західній Україні."},
            {"name": "Буг", "latitude": 49.426, "longitude": 27.001, "description": "Основна річка у південно-західній Україні."}
        ]

        for body in water_bodies:
            water_body, created = WaterBody.objects.get_or_create(
                name=body['name'],
                latitude=body['latitude'],
                longitude=body['longitude'],
                description=body['description']
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Created water body: {water_body.name}'))

        # Populate water quality reports
        water_bodies = WaterBody.objects.all()

        for water_body in water_bodies:
            for year in range(2013, 2024):  # Generate reports for the last decade
                for month in range(1, 13):
                    report = WaterQualityReport.objects.create(
                        water_body=water_body,
                        date=f'{year}-{month:02d}-{random.randint(1, 28):02d}',
                        pollution_level=random.uniform(0, 100),
                        ph_level=random.uniform(6.0, 9.0),
                        temperature=random.uniform(5, 25)
                    )
                    self.stdout.write(self.style.SUCCESS(f'Added report for {water_body.name}: {report.date}'))

        self.stdout.write(self.style.SUCCESS('Database populated with sample data for the last decade.'))
