# Generated by Django 5.1.7 on 2025-03-15 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_alter_orderlineitem_lineitem_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='lineitem_total',
            field=models.DecimalField(decimal_places=4, editable=False, max_digits=20),
        ),
    ]
