# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 17:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('production_count', models.IntegerField(default=0)),
                ('sale_count', models.IntegerField(default=0)),
                ('discount', models.IntegerField(default=0)),
                ('is_free', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('unit', models.CharField(max_length=255, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('photo', models.ImageField(null=True, upload_to='personnel')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beykam.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='inventory',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beykam.Supplier'),
        ),
        migrations.AddField(
            model_name='activity',
            name='personnel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beykam.Personnel'),
        ),
        migrations.AddField(
            model_name='activity',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beykam.Product'),
        ),
    ]
