# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-24 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartflo', '0004_dashboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard',
            name='icon',
            field=models.CharField(default='cogs', max_length=60, verbose_name='Icon'),
            preserve_default=False,
        ),
    ]
