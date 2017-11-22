# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 00:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0007_auto_20171115_0220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
        migrations.RemoveField(
            model_name='article',
            name='article_img',
        ),
        migrations.AddField(
            model_name='article',
            name='article_background',
            field=models.ImageField(default='img/background/background.jpg', upload_to='img/background/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_text',
            field=tinymce.models.HTMLField(verbose_name='Article Content'),
        ),
    ]
