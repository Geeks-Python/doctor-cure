# Generated by Django 4.0 on 2021-12-30 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0003_doctor_fathi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='fathi',
            new_name='user',
        ),
    ]
