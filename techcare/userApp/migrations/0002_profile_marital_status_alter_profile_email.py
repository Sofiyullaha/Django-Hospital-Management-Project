# Generated by Django 4.2.3 on 2023-08-16 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userApp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="marital_status",
            field=models.CharField(
                choices=[
                    ("Single", "Single"),
                    ("Married", "Married"),
                    ("Divorce", "Divorce"),
                    ("Complicated", "Complicated"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="email",
            field=models.EmailField(
                default=None, max_length=50, null=True, unique=True
            ),
        ),
    ]
