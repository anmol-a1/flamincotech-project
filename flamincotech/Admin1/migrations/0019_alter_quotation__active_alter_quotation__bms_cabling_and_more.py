# Generated by Django 4.0.4 on 2022-09-03 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin1', '0018_quotation__trays2_alter_quotation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='_Active',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='_Bms_Cabling',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='_Bms_Piping',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='_Bms_Sensors',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='_Bms_Trays',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='_Ddc',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='_Efforts',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='_Ethernet',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='_Fiber',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='_Others',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='_Third_Party',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='_Trays2',
            field=models.CharField(default='', max_length=200),
        ),
    ]
