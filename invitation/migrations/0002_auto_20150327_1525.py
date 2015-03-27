# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='invite_id',
            field=models.SlugField(default=0, unique=True, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 27, 12, 25, 39, 859354, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 27, 12, 25, 39, 859354, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
    ]
