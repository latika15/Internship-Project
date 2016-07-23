# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('components', '0035_auto_20150810_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion',
            name='suggestion_vote',
            field=models.IntegerField(default=b'0'),
        ),
        migrations.AddField(
            model_name='suggestion',
            name='voters',
            field=models.ManyToManyField(related_name='voted_suggestions', to=settings.AUTH_USER_MODEL),
        ),
    ]
