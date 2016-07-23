# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0020_auto_20150728_1437'),
    ]

    operations = [
        migrations.RenameField(
            model_name='govofficialtable',
            old_name='issue_id',
            new_name='issue',
        ),
    ]
