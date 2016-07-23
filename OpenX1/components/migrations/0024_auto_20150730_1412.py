# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0023_auto_20150728_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestion',
            name='suggestion_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
