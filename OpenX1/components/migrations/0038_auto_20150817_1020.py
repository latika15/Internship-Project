# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0037_suggestion_suggestion_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion',
            name='is_accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='suggestion_category',
            field=models.ForeignKey(to='components.Category'),
        ),
    ]
