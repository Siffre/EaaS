# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-01 07:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommandLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proxy_log_id', models.IntegerField(db_index=True)),
                ('user', models.CharField(db_index=True, max_length=48)),
                ('asset', models.CharField(db_index=True, max_length=128)),
                ('system_user', models.CharField(db_index=True, max_length=48)),
                ('command_no', models.IntegerField()),
                ('command', models.CharField(blank=True, db_index=True, max_length=1000)),
                ('output', models.TextField(blank=True)),
                ('timestamp', models.FloatField(db_index=True)),
            ],
            options={
                'ordering': ['command_no', 'command'],
            },
        ),
        migrations.CreateModel(
            name='LoginLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='Username')),
                ('name', models.CharField(blank=True, max_length=20, verbose_name='Name')),
                ('login_type', models.CharField(choices=[('W', 'Web'), ('ST', 'SSH Terminal'), ('WT', 'Web Terminal')], max_length=2, verbose_name='Login type')),
                ('login_ip', models.GenericIPAddressField(verbose_name='Login ip')),
                ('login_city', models.CharField(blank=True, max_length=254, null=True, verbose_name='Login city')),
                ('user_agent', models.CharField(blank=True, max_length=254, null=True, verbose_name='User agent')),
                ('date_login', models.DateTimeField(auto_now_add=True, verbose_name='Date login')),
            ],
            options={
                'ordering': ['-date_login', 'username'],
                'db_table': 'login_log',
            },
        ),
        migrations.CreateModel(
            name='ProxyLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateTimeField(auto_created=True, verbose_name='Date start')),
                ('user', models.CharField(max_length=32, verbose_name='User')),
                ('asset', models.CharField(max_length=32, verbose_name='Asset')),
                ('system_user', models.CharField(max_length=32, verbose_name='System user')),
                ('login_type', models.CharField(blank=True, choices=[('ST', 'SSH Terminal'), ('WT', 'Web Terminal')], max_length=2, null=True, verbose_name='Login type')),
                ('terminal', models.CharField(blank=True, max_length=32, null=True, verbose_name='Terminal')),
                ('is_failed', models.BooleanField(default=False, verbose_name='Did connect failed')),
                ('is_finished', models.BooleanField(default=False, verbose_name='Is finished')),
                ('date_finished', models.DateTimeField(null=True, verbose_name='Date finished')),
            ],
            options={
                'ordering': ['-date_start', 'user'],
            },
        ),
        migrations.CreateModel(
            name='RecordLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proxy_log_id', models.IntegerField(db_index=True)),
                ('output', models.TextField(verbose_name='Output')),
                ('timestamp', models.FloatField(db_index=True)),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
    ]
