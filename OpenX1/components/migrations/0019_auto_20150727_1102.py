# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0018_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='customerissue',
            name='issue_location',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='customerissue',
            name='issue_img',
            field=models.ImageField(upload_to=b'images/%Y/%m/%d', blank=True),
        ),
    ]
