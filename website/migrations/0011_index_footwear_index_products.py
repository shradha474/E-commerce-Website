# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-14 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_index_salwar_index_sarees'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index_footwear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=250)),
                ('image_title', models.CharField(max_length=500)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('footwear_pic', models.FileField(upload_to='images/footwear')),
            ],
        ),
        migrations.CreateModel(
            name='Index_products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=250)),
                ('image_title', models.CharField(max_length=500)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('product_pic', models.FileField(upload_to='images/product')),
            ],
        ),
    ]