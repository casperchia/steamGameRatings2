# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SGRapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='negative',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='positive',
            field=models.IntegerField(default=0),
        ),
    ]
