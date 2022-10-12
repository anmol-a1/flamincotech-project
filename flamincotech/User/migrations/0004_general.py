# Generated by Django 4.0.4 on 2022-09-27 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_delete_general'),
    ]

    operations = [
        migrations.CreateModel(
            name='General',
            fields=[
                ('sr_no', models.IntegerField(primary_key=True, serialize=False)),
                ('Make', models.CharField(default=' ', max_length=300)),
                ('Model', models.CharField(default=' ', max_length=300)),
                ('Hardware_Items', models.CharField(default=' ', max_length=300)),
                ('Qty', models.IntegerField(default=0)),
                ('Uom', models.CharField(default=' Per Device', max_length=100)),
                ('Cost_Supply_Rate', models.IntegerField(default=0)),
                ('Cost_Supply_Total', models.IntegerField(default=0)),
                ('Cost_Installation_Rate', models.IntegerField(default=0)),
                ('Cost_Installation_Total', models.IntegerField(default=0)),
                ('MRS_Rate', models.IntegerField(default=0)),
                ('MRS_Total', models.IntegerField(default=0)),
                ('MRI_Rate', models.IntegerField(default=0)),
                ('MRI_Total', models.IntegerField(default=0)),
                ('Supply_Rate', models.IntegerField(default=0)),
                ('Supply_Total', models.IntegerField(default=0)),
                ('Installation_Rate', models.IntegerField(default=0)),
                ('Installation_Total', models.IntegerField(default=0)),
                ('Remarks', models.CharField(default=' ', max_length=300)),
                ('Minimum_Qty', models.IntegerField(default=0)),
                ('Minimum_Installation', models.IntegerField(default=0)),
            ],
        ),
    ]