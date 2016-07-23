# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('components', '0007_auto_20150717_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerissue',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 7, 20, 20, 18, 40, 664000, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customerissue',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 7, 20, 20, 18, 59, 268000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customerissue',
            name='votes',
            field=models.ManyToManyField(related_name='votes', to=settings.AUTH_USER_MODEL),
        ),
    ]
