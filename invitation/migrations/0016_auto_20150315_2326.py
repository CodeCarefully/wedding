# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0015_auto_20150315_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='date_opened',
            field=models.DateTimeField(default=datetime.datetime(2000, 1, 1, 0, 0)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 15, 21, 26, 53, 298818, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 15, 21, 26, 53, 298818, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
    ]
