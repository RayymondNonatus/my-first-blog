# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-06-08 17:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_time_mascote'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Jogo',
        ),
    ]
