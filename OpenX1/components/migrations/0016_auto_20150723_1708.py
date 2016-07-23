# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0015_auto_20150723_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_icon',
            field=models.ImageField(upload_to=b'images/', blank=True),
        ),
        migrations.AlterField(
            model_name='customerissue',
            name='issue_img',
            field=models.ImageField(upload_to=b'images/', blank=True),
        ),
    ]
