# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0006_auto_20150310_2314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitation',
            name='date_modified',
        ),
        migrations.AlterField(
            model_name='invitation',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 3, 10, 21, 14, 58, 497290, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 3, 10, 21, 14, 58, 497290, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
