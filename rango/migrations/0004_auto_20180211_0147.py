# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-11 01:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_auto_20180211_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(),
        ),
    ]
