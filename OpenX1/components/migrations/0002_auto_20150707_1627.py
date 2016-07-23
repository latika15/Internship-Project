# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('components', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerIssue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('short_description', models.TextField(max_length=200)),
                ('issue_date', models.DateTimeField(verbose_name=b'Issue Date')),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='category_text',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='subcategory_text',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='customerissue',
            name='subcategory_text',
            field=models.ForeignKey(to='components.SubCategory'),
        ),
        migrations.AddField(
            model_name='customerissue',
            name='username',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
