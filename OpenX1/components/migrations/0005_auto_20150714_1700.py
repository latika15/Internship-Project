# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0004_auto_20150714_1405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerissue',
            old_name='short_description',
            new_name='issue_description',
        ),
    ]
