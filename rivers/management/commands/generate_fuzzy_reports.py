import os
import csv
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from rivers.models import WaterBody, WaterQualityReport, ReportFile
from rivers.fuzzy_logic import calculate_water_quality

class Command(BaseCommand):
    help = 'Generate CSV reports including fuzzy logic results for water bodies and save them in the database.'

    def handle(self, *args, **kwargs):
        # Directory to save reports
        output_dir = 'generated_reports'
        os.makedirs(output_dir, exist_ok=True)

        # Retrieve all water bodies
        water_bodies = WaterBody.objects.all()

        for water_body in water_bodies:
            file_name = f'{water_body.name}_report.csv'
            file_path = os.path.join(output_dir, file_name)

            with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)

                # Write the header row
                writer.writerow([
                    'Date',
                    'Pollution Level',
                    'pH Level',
                    'Temperature',
                    'Fuzzy Quality Score',
                    'Fuzzy Quality Description'
                ])

                # Retrieve all quality reports for the water body
                reports = WaterQualityReport.objects.filter(water_body=water_body).order_by('date')

                for report in reports:
                    # Calculate fuzzy logic result
                    fuzzy_result = calculate_water_quality(
                        pollution_level=report.pollution_level,
                        ph=report.ph_level,
                        temp=report.temperature
                    )

                    # Write the data row
                    writer.writerow([
                        report.date,
                        f'{report.pollution_level:.2f}',
                        f'{report.ph_level:.2f}',
                        f'{report.temperature:.2f}',
                        f'{fuzzy_result["score"]:.2f}',
                        fuzzy_result["description"]
                    ])

            # Save the file in the database
            with open(file_path, 'rb') as f:
                report_file = ReportFile.objects.create(
                    title=f'Звіт для {water_body.name}',
                    file=ContentFile(f.read(), name=file_name)
                )
                self.stdout.write(self.style.SUCCESS(f'Report added to database: {report_file.title}'))

        self.stdout.write(self.style.SUCCESS('All reports have been successfully generated and saved in the database.'))
