# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-22 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flash', '0004_auto_20170622_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.URLField(max_length=1000),
        ),
    ]
