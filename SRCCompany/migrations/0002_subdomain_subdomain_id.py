# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-09 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SRCCompany', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subdomain',
            name='subdomain_id',
            field=models.IntegerField(null=True, verbose_name='子域名编号'),
        ),
    ]