# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-24 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jordanbeach', '0003_auto_20160724_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='poster',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='poster',
            name='state',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
