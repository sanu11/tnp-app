# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-14 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('criteria', models.FloatField()),
                ('salary', models.IntegerField()),
                ('reg_start_date', models.DateTimeField()),
                ('reg_end_date', models.DateTimeField()),
                ('ppt_date', models.DateTimeField()),
                ('apti_date', models.DateTimeField()),
                ('interview_date', models.DateTimeField()),
                ('hired_people', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=60, unique=True)),
                ('password', models.CharField(max_length=12)),
                ('phone', models.CharField(max_length=10)),
                ('branch', models.CharField(max_length=6)),
                ('average', models.FloatField()),
                ('placed', models.CharField(default='No', max_length=4)),
                ('active_back', models.CharField(default='No', max_length=4)),
                ('company_id', models.IntegerField(default=-1)),
            ],
        ),
    ]
