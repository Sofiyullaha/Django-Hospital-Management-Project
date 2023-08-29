# Generated by Django 4.2.3 on 2023-08-23 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Service",
            fields=[
                ("service_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "service_option",
                    models.CharField(
                        choices=[
                            ("Emergency Care", "Emergency Care"),
                            ("Operation & Surgery", "Operation & Surgery"),
                            ("Outdoor Checkup", "Outdoor Checkup"),
                            ("Ambulance Service", "Ambulance Service"),
                            ("Medicine & Pharmacy", "Medicine & Pharmacy"),
                            ("Blood Testing", "Blood Testing"),
                        ],
                        max_length=20,
                        unique=True,
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                (
                    "service_logo",
                    models.ImageField(blank=True, null=True, upload_to="service_logo/"),
                ),
                ("price", models.BigIntegerField()),
                (
                    "description",
                    models.CharField(blank=True, max_length=300, null=True),
                ),
                (
                    "HoD",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
