# Generated by Django 4.2.3 on 2023-08-28 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("servicesApp", "0003_remove_bookingservice_service_option_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookingservice",
            name="service_name",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
