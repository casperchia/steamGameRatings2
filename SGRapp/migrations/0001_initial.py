# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('appid', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('positive', models.IntegerField(default=0)),
                ('negative', models.IntegerField(default=0)),
                ('rating', models.DecimalField(editable=False, max_digits=5, decimal_places=2)),
                ('wilson', models.DecimalField(editable=False, max_digits=5, decimal_places=2)),
            ],
        ),
    ]
