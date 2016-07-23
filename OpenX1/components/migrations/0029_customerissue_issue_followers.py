# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0028_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerissue',
            name='issue_followers',
            field=models.IntegerField(default=0),
        ),
    ]
