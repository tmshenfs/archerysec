# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-25 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staticscanners', '0003_auto_20190125_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bandit_scan_db',
            name='SEVERITY_LOW',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]