# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20170419_0940'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название мероприятия', max_length=200)),
                ('date', models.DateField(help_text='Дата проведения мероприятия')),
                ('description', models.TextField(help_text='Описание мероприятия')),
                ('registration', models.BooleanField(help_text='Регистрация на мероприятие: обзательна или нет')),
                ('location', models.CharField(help_text='Место проведения мероприятия', max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Events',
        ),
    ]
