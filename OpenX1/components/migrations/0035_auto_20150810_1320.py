# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0034_auto_20150810_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='govtable',
            name='subcategory',
            field=models.ForeignKey(to='components.SubCategory'),
        ),
    ]
