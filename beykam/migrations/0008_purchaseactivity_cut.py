# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-25 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beykam', '0007_auto_20161225_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseactivity',
            name='cut',
            field=models.IntegerField(default=30),
        ),
    ]
