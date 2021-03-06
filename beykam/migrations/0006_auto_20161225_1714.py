# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-25 17:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beykam', '0005_auto_20161225_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('personnel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beykam.Personnel')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beykam.Product')),
            ],
        ),
        migrations.CreateModel(
            name='SaleActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.IntegerField(default=0)),
                ('is_free', models.BooleanField(default=False)),
                ('personnel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beykam.Personnel')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beykam.Product')),
            ],
        ),
        migrations.RemoveField(
            model_name='activity',
            name='personnel',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='product',
        ),
        migrations.DeleteModel(
            name='Activity',
        ),
    ]
