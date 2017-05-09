# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-27 09:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=60)),
                ('cylinders', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Layouts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('layout', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='bikes',
            name='layout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bike_selector.models.Layout'),
        ),
        migrations.AddField(
            model_name='bikes',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bike_selector.models.Manufacturer'),
        ),
    ]