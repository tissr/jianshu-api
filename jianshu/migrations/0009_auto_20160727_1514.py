# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-27 15:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jianshu', '0008_auto_20160727_1024'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='search_article',
            new_name='SearchArticle',
        ),
    ]
