# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0009_auto_20150720_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerissue',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='customerissue',
            name='issue_vote',
        ),
        migrations.AddField(
            model_name='customerissue',
            name='issue_vote',
            field=models.IntegerField(default=b'1'),
        ),
    ]
