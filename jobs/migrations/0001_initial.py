# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('referencenumber', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('sourcename', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]
