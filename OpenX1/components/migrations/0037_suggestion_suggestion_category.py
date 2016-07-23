# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0036_auto_20150811_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion',
            name='suggestion_category',
            field=models.ForeignKey(default=b'', to='components.Category'),
        ),
    ]
