# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-26 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beykam', '0015_auto_20161226_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseactivity',
            name='cut',
        ),
        migrations.AddField(
            model_name='personnel',
            name='cut',
            field=models.DecimalField(decimal_places=2, default=30, max_digits=10),
        ),
    ]