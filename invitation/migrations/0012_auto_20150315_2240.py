# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0011_auto_20150315_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='invitation_name',
            field=models.CharField(blank=True, default='', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 3, 15, 20, 40, 47, 407579, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='personal_message',
            field=models.CharField(blank=True, default='', max_length=400),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='diet_info',
            field=models.CharField(blank=True, default='', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.CharField(blank=True, default='', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='has_car_room_location',
            field=models.CharField(blank=True, default='', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 3, 15, 20, 40, 47, 407579, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='needs_ride_location',
            field=models.CharField(blank=True, default='', max_length=200),
            preserve_default=True,
        ),
    ]
