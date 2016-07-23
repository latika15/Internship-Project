# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0029_customerissue_issue_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerissue',
            name='issue_title',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='customerissue',
            name='issue_description',
            field=models.TextField(max_length=500),
        ),
    ]
