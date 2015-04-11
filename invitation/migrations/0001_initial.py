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
            name='Invitation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('modified_date', models.DateTimeField(default=datetime.datetime(2015, 4, 11, 9, 46, 56, 899094, tzinfo=utc), auto_now=True)),
                ('with_guest', models.BooleanField(default=False, verbose_name='Invite additional guest (+1)')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
