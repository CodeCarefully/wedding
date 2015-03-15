# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0014_auto_20150315_2258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitation',
            name='was_opened',
        ),
        migrations.AddField(
            model_name='invitation',
            name='date_opened',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 3, 15, 21, 20, 21, 837373, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 3, 15, 21, 20, 12, 675939, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 3, 15, 21, 20, 12, 675939, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
