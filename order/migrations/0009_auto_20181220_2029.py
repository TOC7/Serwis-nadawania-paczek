# Generated by Django 2.1.2 on 2018-12-20 19:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_auto_20181220_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='apartment_number',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
