# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0032_customerissue_voters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broadcastmessage',
            name='broadcast_msg',
            field=models.CharField(default=b'', max_length=1000),
        ),
    ]
