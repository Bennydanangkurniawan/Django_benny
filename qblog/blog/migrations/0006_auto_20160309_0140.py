# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-09 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160307_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portofolio',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]
