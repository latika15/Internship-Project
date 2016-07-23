# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('components', '0008_auto_20150720_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerissue',
            name='name',
        ),
        migrations.RemoveField(
            model_name='customerissue',
            name='votes',
        ),
        migrations.RemoveField(
            model_name='customerissue',
            name='issue_vote',
        ),
        migrations.AddField(
            model_name='customerissue',
            name='issue_vote',
            field=models.ManyToManyField(related_name='issue_vote', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customerissue',
            name='slug',
            field=models.SlugField(default=b'cust_email'),
        ),
    ]
