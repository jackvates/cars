# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 01:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_auto_20160328_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rows_Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rows', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='MetaTable',
        ),
        migrations.DeleteModel(
            name='Row',
        ),
        migrations.DeleteModel(
            name='Table',
        ),
    ]