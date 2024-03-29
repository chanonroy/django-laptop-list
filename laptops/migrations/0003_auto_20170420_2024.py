# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-20 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptops', '0002_auto_20170420_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpu',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='gpu',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='laptop',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='laptop',
            name='year',
            field=models.IntegerField(default=2016),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
