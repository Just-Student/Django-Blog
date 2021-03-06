# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20171114_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_subheading',
            field=models.CharField(default='this is a nice article', max_length=200),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_text',
            field=models.TextField(default='Nice text!'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_title',
            field=models.CharField(default='a nice article', max_length=200),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comments_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
