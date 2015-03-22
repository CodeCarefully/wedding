# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0002_auto_20150223_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 25, 19, 46, 31, 224525, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invitation',
            name='invitation_total_rsvp',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
