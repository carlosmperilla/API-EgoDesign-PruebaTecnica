# Generated by Django 3.2.19 on 2023-05-28 04:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelosautos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeloauto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=11, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(999999999.0)], verbose_name='Precio'),
        ),
    ]
