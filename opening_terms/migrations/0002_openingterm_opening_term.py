# Generated by Django 2.2.4 on 2019-12-11 05:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('opening_terms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='openingterm',
            name='opening_term',
            field=models.FileField(default=django.utils.timezone.now, upload_to='opening_terms_files'),
            preserve_default=False,
        ),
    ]
