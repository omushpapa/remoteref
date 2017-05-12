# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-12 06:43
from __future__ import unicode_literals

import debtinfo.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Debtor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=10)),
                ('cell', models.CharField(max_length=12)),
                ('debtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debtor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=10)),
                ('cell', models.CharField(max_length=12)),
                ('amount', debtinfo.models.CurrencyField(decimal_places=2, max_digits=11)),
                ('creditor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_creditor', to=settings.AUTH_USER_MODEL)),
                ('debtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_debtor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]