# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mods', '0009_auto_20170424_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='instruction',
            name='deploy',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='instruction',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]