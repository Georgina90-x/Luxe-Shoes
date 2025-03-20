# Generated by Django 5.1.7 on 2025-03-20 21:35

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_userprofile_default_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_country',
            field=django_countries.fields.CountryField(default='GB', max_length=2),
        ),
    ]
