# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(verbose_name='Quote')),
                ('is_ok', models.NullBooleanField(verbose_name='Is moderated?')),
                ('added_on', models.DateTimeField(default=datetime.datetime(2015, 2, 25, 16, 9, 32, 994962, tzinfo=utc), verbose_name='Added on')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
