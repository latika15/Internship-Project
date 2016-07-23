# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0030_auto_20150806_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerissue',
            name='issue_vote',
            field=models.IntegerField(default=b'0'),
        ),
    ]
