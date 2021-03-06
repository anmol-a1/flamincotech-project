# Generated by Django 4.0.4 on 2022-05-31 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin1', '0014_remove_desk_booking_solution_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='desk_planning_solution',
            name='id',
        ),
        migrations.RemoveField(
            model_name='desk_utilization_solution',
            name='id',
        ),
        migrations.RemoveField(
            model_name='employee_one_mobile_app',
            name='id',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='id',
        ),
        migrations.RemoveField(
            model_name='human_body_temperature_license',
            name='id',
        ),
        migrations.RemoveField(
            model_name='kiosk_license',
            name='id',
        ),
        migrations.RemoveField(
            model_name='meeting_room_license_booking',
            name='id',
        ),
        migrations.RemoveField(
            model_name='meeting_room_license_occupancy',
            name='id',
        ),
        migrations.RemoveField(
            model_name='meeting_room_license_people_count',
            name='id',
        ),
        migrations.RemoveField(
            model_name='restroom_license_odour',
            name='id',
        ),
        migrations.RemoveField(
            model_name='restroom_license_people_count',
            name='id',
        ),
        migrations.RemoveField(
            model_name='restroom_license_wet_floor_detection',
            name='id',
        ),
        migrations.RemoveField(
            model_name='rostering',
            name='id',
        ),
        migrations.RemoveField(
            model_name='wayfinding',
            name='id',
        ),
        migrations.AddField(
            model_name='desk_planning_solution',
            name='sr_no',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='desk_utilization_solution',
            name='sr_no',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee_one_mobile_app',
            name='sr_no',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedback',
            name='sr_no',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='human_body_temperature_license',
            name='sr_no',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kiosk_license',
            name='sr_no',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meeting_room_license_booking',
            name='sr_no',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meeting_room_license_occupancy',
            name='sr_no',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meeting_room_license_people_count',
            name='sr_no',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restroom_license_odour',
            name='sr_no',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restroom_license_people_count',
            name='sr_no',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restroom_license_wet_floor_detection',
            name='sr_no',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rostering',
            name='sr_no',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wayfinding',
            name='sr_no',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
