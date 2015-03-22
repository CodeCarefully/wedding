# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0025_auto_20150318_2310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitation',
            name='guest_rsvp',
        ),
        migrations.AlterField(
            model_name='invitation',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 22, 21, 0, 53, 198151, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 22, 21, 0, 53, 198151, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
    ]
