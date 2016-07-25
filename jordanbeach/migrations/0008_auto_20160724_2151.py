# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-24 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jordanbeach', '0007_auto_20160724_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='journal_issue',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='journal_vol',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='talk',
            name='venue',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teaching',
            name='course_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teaching',
            name='course_venue',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teaching',
            name='mentee',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teaching',
            name='mentee_role',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teaching',
            name='year_end',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]