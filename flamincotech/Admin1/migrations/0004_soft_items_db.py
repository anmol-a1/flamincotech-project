# Generated by Django 4.0.4 on 2022-08-13 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin1', '0003_margin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Soft_Items_DB',
            fields=[
                ('sr_no', models.AutoField(primary_key=True, serialize=False)),
                ('Make', models.CharField(default='Flamencotech', max_length=100)),
                ('Model', models.CharField(default='DB V3.3', max_length=100)),
                ('Item', models.CharField(max_length=300)),
                ('Qty', models.IntegerField(default=0)),
                ('UOM', models.CharField(default='Per Item', max_length=50)),
                ('Capex', models.IntegerField(default=0)),
                ('C_Total', models.IntegerField(default=0)),
                ('Opex', models.IntegerField(default=0)),
                ('O_Total', models.IntegerField(default=0)),
            ],
        ),
    ]
