# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0038_auto_20150817_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestion',
            name='suggestion_category',
            field=models.ForeignKey(default=b'', to='components.Category'),
        ),
    ]
