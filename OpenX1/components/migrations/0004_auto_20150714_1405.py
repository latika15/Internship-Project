# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0003_auto_20150714_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerissue',
            name='issue_subcategory',
            field=models.CharField(max_length=50),
        ),
    ]
