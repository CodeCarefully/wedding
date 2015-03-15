# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0012_auto_20150315_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='was_opened',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 3, 15, 20, 54, 0, 701258, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 3, 15, 20, 54, 0, 701258, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
