# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-06-03 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watson', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='language_code',
            field=models.CharField(max_length=10),
        ),
    ]