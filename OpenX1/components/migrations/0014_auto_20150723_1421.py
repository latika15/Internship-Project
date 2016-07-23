# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0013_customerissue_issue_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerissue',
            name='issue_img',
            field=models.ImageField(default=b'', upload_to=b'images'),
        ),
    ]
