# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appbooker', '0003_auto_20180327_0330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='date',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='time',
        ),
        migrations.AddField(
            model_name='appointment',
            name='datetime',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
