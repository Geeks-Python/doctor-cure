# Generated by Django 4.0 on 2021-12-29 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pharmacy', '0005_rename_country_pharmacy_address_pharmacy_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pharmacy',
            old_name='address',
            new_name='building_number',
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='street',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='town',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
