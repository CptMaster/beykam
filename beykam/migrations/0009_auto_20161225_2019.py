# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-25 20:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beykam', '0008_purchaseactivity_cut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2016, 12, 25), null=True),
        ),
    ]
