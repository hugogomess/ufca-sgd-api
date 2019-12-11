# Generated by Django 2.2.4 on 2019-10-28 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demands', '0002_demand_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demand',
            name='status',
            field=models.CharField(choices=[('ABERTA', 'ABERTA'), ('FECHADA', 'FECHADA')], default='ABERTA', max_length=20),
        ),
    ]