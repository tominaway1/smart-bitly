# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-06-03 20:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watson', '0002_auto_20170603_1850'),
        ('htmlparser', '0004_auto_20170603_1850'),
    ]

    operations = [
        migrations.CreateModel(
            name='Html_Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('html_source', models.TextField()),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watson.Language')),
            ],
        ),
        migrations.RemoveField(
            model_name='urlproperties',
            name='html_source',
        ),
        migrations.AddField(
            model_name='html_content',
            name='url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='htmlparser.UrlProperties'),
        ),
    ]