# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('components', '0010_auto_20150720_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('suggestion_title', models.CharField(max_length=100)),
                ('suggestion_description', models.TextField(help_text=b'This is required field', max_length=500)),
                ('suggestion_date', models.DateField(auto_now_add=True)),
                ('username', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='customerissue',
            name='cust_email',
        ),
        migrations.AddField(
            model_name='customerissue',
            name='username',
            field=models.ForeignKey(default=b'', to=settings.AUTH_USER_MODEL),
        ),
    ]
