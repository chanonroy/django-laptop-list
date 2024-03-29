# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-20 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptops', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cpu',
            options={'verbose_name_plural': 'CPUs'},
        ),
        migrations.AlterModelOptions(
            name='gpu',
            options={'verbose_name_plural': 'GPUs'},
        ),
        migrations.RenameField(
            model_name='cpu',
            old_name='clock_speed',
            new_name='clock_speed_max',
        ),
        migrations.AddField(
            model_name='cpu',
            name='clock_speed_min',
            field=models.FloatField(default='1', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gpu',
            name='memory',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
