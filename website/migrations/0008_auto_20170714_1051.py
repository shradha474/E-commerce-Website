# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-14 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index_jeans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=250)),
                ('image_title', models.CharField(max_length=500)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('jeans_pic', models.FileField(upload_to='images/jeans')),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user_name',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
