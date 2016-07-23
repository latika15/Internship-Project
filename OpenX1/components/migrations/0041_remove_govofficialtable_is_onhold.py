# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0040_auto_20150817_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='govofficialtable',
            name='is_OnHold',
        ),
    ]
