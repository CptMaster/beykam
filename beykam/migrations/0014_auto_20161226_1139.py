# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-26 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beykam', '0013_auto_20161226_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseactivity',
            name='total',
            field=models.DecimalField(decimal_places=2, default=30, max_digits=10),
        ),
        migrations.AlterField(
            model_name='saleactivity',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
