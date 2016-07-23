# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0016_auto_20150723_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_icon',
        ),
    ]
