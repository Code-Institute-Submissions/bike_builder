# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-04 09:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='public_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
