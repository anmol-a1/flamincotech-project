# Generated by Django 3.2.13 on 2022-04-25 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin1', '0004_vpss'),
    ]

    operations = [
        migrations.AddField(
            model_name='vpss',
            name='Unit_Price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
