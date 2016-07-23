# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0024_auto_20150730_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='broadcast_msgTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('broadcast_msg', models.CharField(max_length=1000)),
                ('broadcast_date', models.DateTimeField(auto_now_add=True)),
                ('username', models.ForeignKey(to='components.govTable')),
            ],
        ),
    ]
