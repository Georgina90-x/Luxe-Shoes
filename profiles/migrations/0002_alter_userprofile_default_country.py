# Generated by Django 5.1.7 on 2025-03-18 00:47

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
    ]
