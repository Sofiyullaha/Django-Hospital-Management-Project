# Generated by Django 4.2.3 on 2023-09-04 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("servicesApp", "0004_bookingservice_service_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="PatientMedicalHHistory",
            fields=[
                ("report_id", models.AutoField(primary_key=True, serialize=False)),
                ("date_created", models.DateField(auto_now_add=True)),
                ("next_approved_date", models.DateField(blank=True, null=True)),
                ("next_approved_time", models.TimeField(blank=True, null=True)),
                ("description", models.CharField(blank=True, max_length=300)),
                (
                    "service_name",
                    models.CharField(blank=True, max_length=300, null=True),
                ),
                (
                    "patient_status",
                    models.CharField(
                        choices=[
                            ("Unknown", "Unknown"),
                            ("Booked for Test", "Booked for Test"),
                            ("Transferred", "Transferred"),
                            ("Admitted", "Admitted"),
                            ("Discharged", "Discharged"),
                            ("Dead", "Dead"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "doctor_remark",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "approved_doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="approved_doctor",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="servicesApp.service",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
