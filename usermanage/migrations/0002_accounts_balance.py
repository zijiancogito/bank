# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 02:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
            preserve_default=False,
        ),
    ]
