# Generated by Django 4.2.17 on 2024-12-16 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("rivers", "0003_monitoringstation_latitude_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ReportFile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200, verbose_name="Назва звіту")),
                (
                    "file",
                    models.FileField(upload_to="reports/", verbose_name="Файл звіту"),
                ),
                (
                    "uploaded_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата завантаження"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WaterBody",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="Назва водойми"
                    ),
                ),
                ("latitude", models.FloatField(verbose_name="Широта")),
                ("longitude", models.FloatField(verbose_name="Довгота")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Опис"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WaterQualityReport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(verbose_name="Дата звіту")),
                (
                    "pollution_level",
                    models.FloatField(verbose_name="Рівень забруднення"),
                ),
                ("ph_level", models.FloatField(verbose_name="pH рівень")),
                ("temperature", models.FloatField(verbose_name="Температура (°C)")),
                (
                    "water_body",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="quality_reports",
                        to="rivers.waterbody",
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="ecologicalindicator",
            name="river",
        ),
        migrations.RemoveField(
            model_name="measurement",
            name="river",
        ),
        migrations.RemoveField(
            model_name="measurement",
            name="station",
        ),
        migrations.RemoveField(
            model_name="monitoringstation",
            name="river",
        ),
        migrations.DeleteModel(
            name="SensorData",
        ),
        migrations.DeleteModel(
            name="EcologicalIndicator",
        ),
        migrations.DeleteModel(
            name="Measurement",
        ),
        migrations.DeleteModel(
            name="MonitoringStation",
        ),
        migrations.DeleteModel(
            name="River",
        ),
    ]
