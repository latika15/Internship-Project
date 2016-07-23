# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0019_auto_20150727_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerissue',
            name='issue_img',
            field=models.ImageField(upload_to=b'images/', blank=True),
        ),
    ]
