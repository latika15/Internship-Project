# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0021_auto_20150728_1703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='govofficialtable',
            old_name='issue',
            new_name='issue1',
        ),
    ]
