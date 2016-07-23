# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0014_auto_20150723_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerissue',
            name='issue_img',
            field=models.FileField(upload_to=b'images/', blank=True),
        ),
    ]
