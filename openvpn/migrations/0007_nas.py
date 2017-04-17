# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openvpn', '0006_auto_20170416_2320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nasname', models.CharField(max_length=128)),
                ('shortname', models.CharField(max_length=32)),
                ('type', models.CharField(max_length=30)),
                ('ports', models.IntegerField(blank=True, null=True)),
                ('secret', models.CharField(max_length=60)),
                ('server', models.CharField(blank=True, max_length=64, null=True)),
                ('community', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]