# Generated by Django 3.1.7 on 2021-05-13 16:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20210513_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conf_mes',
            name='criado_em',
            field=models.DateField(default=datetime.datetime(2021, 5, 13, 16, 16, 52, 855242, tzinfo=utc), verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='diario',
            name='criado_em',
            field=models.DateField(default=datetime.datetime(2021, 5, 13, 16, 16, 52, 852706, tzinfo=utc), verbose_name='Criado em'),
        ),
        migrations.AlterField(
            model_name='obitos_mes',
            name='criado_em',
            field=models.DateField(default=datetime.datetime(2021, 5, 13, 16, 16, 52, 854589, tzinfo=utc), verbose_name='Criado em'),
        ),
    ]