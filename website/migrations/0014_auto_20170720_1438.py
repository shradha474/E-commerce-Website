# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-20 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_index_kids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index_kids',
            name='Description',
            field=models.CharField(max_length=2500),
        ),
    ]
