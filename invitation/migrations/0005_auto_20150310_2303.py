# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0004_auto_20150225_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='personal_message',
            field=models.CharField(default=' ', max_length=400),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='car_room_amount',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='diet_info',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='has_car_room_location',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='is_vegan',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='needs_ride_location',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 10, 21, 3, 8, 835789, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=True,
        ),
    ]
