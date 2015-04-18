# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0008_auto_20150411_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='invitation_name',
            field=models.CharField(max_length=200, blank=True, default='', verbose_name='Invite name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 18, 18, 56, 26, 439297, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 18, 18, 56, 26, 439297, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
    ]
