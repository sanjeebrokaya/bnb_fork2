# Generated by Django 5.0.9 on 2024-10-07 11:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="photo",
            field=models.ImageField(upload_to="images"),
        ),
    ]
