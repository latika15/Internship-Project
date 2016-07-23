# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0002_auto_20150707_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_text',
            new_name='category_name',
        ),
        migrations.RenameField(
            model_name='customerissue',
            old_name='subcategory_text',
            new_name='issue_subcategory',
        ),
        migrations.RenameField(
            model_name='subcategory',
            old_name='subcategory_text',
            new_name='subcategory_name',
        ),
        migrations.RemoveField(
            model_name='customerissue',
            name='username',
        ),
        migrations.AddField(
            model_name='customerissue',
            name='cust_email',
            field=models.EmailField(default=b'', max_length=254),
        ),
        migrations.AddField(
            model_name='customerissue',
            name='issue_vote',
            field=models.IntegerField(default=b'1'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='subcategory_description',
            field=models.TextField(default=b'', max_length=400),
        ),
        migrations.AlterField(
            model_name='customerissue',
            name='issue_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
