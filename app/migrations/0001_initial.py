# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-07 11:21
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
                ('criteria', models.FloatField(blank=True, null=True)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('back', models.CharField(blank=True, max_length=100, null=True)),
                ('ppt_date', models.DateTimeField(blank=True, null=True)),
                ('other_details', models.CharField(blank=True, max_length=1000, null=True)),
                ('reg_start_date', models.DateTimeField(blank=True, null=True)),
                ('reg_end_date', models.DateTimeField(blank=True, null=True)),
                ('reg_link', models.CharField(blank=True, max_length=1000, null=True)),
                ('hired_people', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=200)),
                ('message', models.CharField(default='', max_length=10000)),
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
        migrations.CreateModel(
            name='Verify',
            fields=[
                ('v_id', models.AutoField(primary_key=True, serialize=False)),
                ('prn', models.CharField(max_length=50)),
            ],
        ),
    ]
