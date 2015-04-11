# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0002_auto_20150411_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='invite_id',
            field=models.SlugField(editable=False, default=1, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 4, 11, 9, 49, 47, 11013, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
