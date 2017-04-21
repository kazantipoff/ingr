# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('weapon', '0002_delete_weapon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('type', models.CharField(choices=[('Virus', 'захватывающее'), ('Weapon', 'разрушающее')], max_length=6)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]