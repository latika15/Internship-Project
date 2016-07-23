# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0011_auto_20150723_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerissue',
            name='username',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
