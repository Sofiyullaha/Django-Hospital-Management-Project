# Generated by Django 4.2.3 on 2023-09-06 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("userApp", "0002_profile_marital_status_alter_profile_email"),
        ("servicesApp", "0007_remove_bookingservice_patient_status_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment_service",
            fields=[
                ("payment_id", models.AutoField(primary_key=True, serialize=False)),
                ("amount", models.BigIntegerField()),
                ("date_of_payment", models.DateTimeField(auto_now_add=True)),
                ("paystack_detail", models.BigIntegerField(unique=True)),
                (
                    "booking",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="servicesApp.bookingservice",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="userApp.profile",
                    ),
                ),
            ],
        ),
    ]