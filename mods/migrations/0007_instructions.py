# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mods', '0006_auto_20170424_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deploy', models.TextField(blank=True, null=True)),
                ('practice', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
