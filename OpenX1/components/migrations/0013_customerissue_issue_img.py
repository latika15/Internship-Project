# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0012_auto_20150723_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerissue',
            name='issue_img',
            field=models.ImageField(default=b'', upload_to=b'pictures'),
        ),
    ]
