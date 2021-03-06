# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 00:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('body', models.TextField()),
                ('publish', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'modif',
                'verbose_name_plural': 'galau',
            },
        ),
    ]
