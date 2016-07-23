# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0006_auto_20150717_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='govofficialtable',
            name='flag',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='govofficialtable',
            name='is_OnHold',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='govofficialtable',
            name='assigned_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
