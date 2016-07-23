# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('components', '0005_auto_20150714_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='govOfficialTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('assigned_date', models.DateField(auto_now=True)),
                ('resolved_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='govTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_superofficial', models.BooleanField(default=False)),
                ('is_deptHead', models.BooleanField(default=False)),
                ('issues_assigned', models.IntegerField(default=b'0')),
                ('issues_resolved', models.IntegerField(default=b'0')),
                ('category', models.ForeignKey(to='components.Category')),
                ('subcategory', models.ForeignKey(to='components.SubCategory')),
                ('username', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='customerissue',
            name='is_assigned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customerissue',
            name='is_resolved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customerissue',
            name='is_seen',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='govofficialtable',
            name='issue_id',
            field=models.ForeignKey(to='components.CustomerIssue'),
        ),
        migrations.AddField(
            model_name='govofficialtable',
            name='username',
            field=models.ForeignKey(to='components.govTable'),
        ),
    ]
