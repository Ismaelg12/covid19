# Generated by Django 3.0.7 on 2021-02-16 17:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210216_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diario',
            name='criado_em',
            field=models.DateField(default=datetime.datetime(2021, 2, 16, 17, 44, 12, 782517, tzinfo=utc), verbose_name='Criado em'),
        ),
    ]
