# Generated by Django 4.0 on 2022-01-03 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0013_appointment_doctor_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='clinic_location',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
