# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-05 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beykam', '0019_auto_20170105_0624'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color_code',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='dimension_code',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
