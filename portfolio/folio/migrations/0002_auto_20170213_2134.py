# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='states',
            name='state_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
