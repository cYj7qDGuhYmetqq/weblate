# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-09-02 09:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("trans", "0002_delete_indexupdate")]

    operations = [
        migrations.RemoveField(model_name="translation", name="commit_message")
    ]
