# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-04 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0004_auto_20180304_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='image_upload',
            field=models.ImageField(null=True, upload_to='pics/'),
        ),
    ]
