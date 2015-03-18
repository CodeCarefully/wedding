# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0021_auto_20150317_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitation',
            name='invitation_total_RSVP',
        ),
        migrations.AlterField(
            model_name='invitation',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 17, 20, 23, 4, 314119, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 17, 20, 23, 4, 314119, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
    ]
