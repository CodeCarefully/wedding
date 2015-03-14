# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0005_auto_20150310_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 10, 21, 14, 7, 665306, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 10, 21, 14, 7, 665306, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 10, 21, 14, 7, 665306, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
