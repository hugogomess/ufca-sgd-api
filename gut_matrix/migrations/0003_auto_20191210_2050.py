# Generated by Django 2.2.4 on 2019-12-10 20:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gut_matrix', '0002_auto_20191210_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gutmatrix',
            name='gut',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(125)]),
        ),
        migrations.AlterField(
            model_name='gutmatrix',
            name='trend',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='gutmatrix',
            name='urgency',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
