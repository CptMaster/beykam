# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-05 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beykam', '0021_auto_20170105_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='children',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]