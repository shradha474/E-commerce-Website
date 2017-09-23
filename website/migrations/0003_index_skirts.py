# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-10 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20170710_0537'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index_skirts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=250)),
                ('image_title', models.CharField(max_length=500)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('skirts_pic', models.FileField(upload_to='images/latest')),
            ],
        ),
    ]