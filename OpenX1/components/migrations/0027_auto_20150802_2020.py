# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0026_remove_broadcast_msgtable_username'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='broadcast_msgTable',
            new_name='BroadcastMessage',
        ),
        migrations.AlterField(
            model_name='govofficialtable',
            name='username',
            field=models.ForeignKey(to='components.GovTable'),
        ),
    ]
