# Generated by Django 3.1.7 on 2021-05-14 01:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20210513_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conf_mes',
            name='criado_em',
            field=models.DateField(default=datetime.datetime(2021, 5, 14, 1, 17, 32, 662109, tzinfo=utc), verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='diario',
            name='criado_em',
            field=models.DateField(default=datetime.datetime(2021, 5, 14, 1, 17, 32, 659733, tzinfo=utc), verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='obitos_mes',
            name='criado_em',
            field=models.DateField(default=datetime.datetime(2021, 5, 14, 1, 17, 32, 661515, tzinfo=utc), verbose_name='Criado em'),
        ),
    ]
