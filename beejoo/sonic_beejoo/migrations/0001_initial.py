# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 13:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('is_displayed', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('is_displayed', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='DesignType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Тип изделия')),
                ('is_displayed', models.BooleanField(default=True, verbose_name='Отображать')),
            ],
            options={
                'verbose_name_plural': 'Состав',
            },
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('short_description', models.CharField(max_length=100)),
                ('full_description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sale', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('full_img_uri', models.ImageField(blank=True, upload_to='goods_img')),
                ('preview_img_uri', models.ImageField(blank=True, upload_to='goods_img')),
                ('data_created', models.DateTimeField(default=datetime.datetime(2016, 11, 22, 13, 57, 39, 938158, tzinfo=utc))),
                ('amount', models.IntegerField(default=1)),
                ('is_displayed', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sonic_beejoo.Category')),
                ('colors', models.ManyToManyField(to='sonic_beejoo.Color')),
                ('design_types', models.ManyToManyField(to='sonic_beejoo.DesignType')),
            ],
        ),
    ]
