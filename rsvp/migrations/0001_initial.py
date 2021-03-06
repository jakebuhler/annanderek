# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-31 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('guest_count', models.IntegerField()),
                ('accommodation_requests', models.TextField(blank=True)),
                ('submitted', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('submitted',),
            },
        ),
    ]
