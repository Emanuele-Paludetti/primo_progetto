# Generated by Django 5.1.4 on 2025-02-18 15:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_articolo_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articolo',
            name='data',
            field=models.DateField(blank=True, default=datetime.datetime(2025, 2, 18, 16, 51, 26, 476446)),
        ),
        migrations.AlterField(
            model_name='giornalista',
            name='anno_di_nascita',
            field=models.DateField(blank=True, default=datetime.datetime(2025, 2, 18, 16, 51, 26, 476190), max_length=10),
        ),
    ]
