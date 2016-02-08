# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-08 00:03
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('code', models.CharField(max_length=8, verbose_name='Code')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
            options={
                'verbose_name_plural': 'Games',
                'ordering': ['-created'],
                'verbose_name': 'Game',
            },
        ),
        migrations.CreateModel(
            name='GameSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(default={})),
            ],
            options={
                'verbose_name_plural': 'Game Settings',
                'ordering': ['-created'],
                'verbose_name': 'Game Settings',
            },
        ),
        migrations.AddField(
            model_name='game',
            name='settings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_api.GameSettings'),
        ),
    ]
