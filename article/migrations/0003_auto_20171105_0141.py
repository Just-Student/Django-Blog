# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 22:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20171105_0138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comments_date',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='comments_likes',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='comments_title',
        ),
    ]
