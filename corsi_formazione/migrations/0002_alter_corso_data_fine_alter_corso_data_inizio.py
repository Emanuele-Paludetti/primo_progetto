# Generated by Django 5.1.3 on 2025-02-26 08:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corsi_formazione', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corso',
            name='data_fine',
            field=models.DateField(blank=True, default=datetime.datetime(2025, 2, 26, 9, 32, 37, 228519)),
        ),
        migrations.AlterField(
            model_name='corso',
            name='data_inizio',
            field=models.DateField(blank=True, default=datetime.datetime(2025, 2, 26, 9, 32, 37, 228519)),
        ),
    ]
