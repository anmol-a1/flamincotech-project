# Generated by Django 4.0.4 on 2022-09-03 05:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin1', '0017_remove_quotation__soft_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='_Trays2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='date',
            field=models.DateField(default=datetime.date(2022, 9, 3)),
        ),
    ]