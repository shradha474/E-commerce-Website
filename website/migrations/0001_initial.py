# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-10 05:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=250)),
                ('image_title', models.CharField(max_length=500)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image_pic', models.FileField(upload_to='images/titles')),
            ],
        ),
    ]
