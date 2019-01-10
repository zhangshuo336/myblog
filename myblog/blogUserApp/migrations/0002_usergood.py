# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-01-10 22:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artDataApp', '0001_initial'),
        ('blogUserApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artDataApp.ArtData')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogUserApp.User')),
            ],
        ),
    ]
