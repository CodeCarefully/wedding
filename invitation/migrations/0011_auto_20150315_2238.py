# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import invitation.models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0010_auto_20150315_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='invite_id',
            field=models.IntegerField(default=invitation.models.id_generator, editable=False, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 15, 20, 38, 21, 147275, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='personal_message',
            field=models.CharField(default='', max_length=400),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='diet_info',
            field=models.CharField(default='', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.CharField(default='', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='english_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='has_car_room_location',
            field=models.CharField(default='', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='hebrew_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 15, 20, 38, 21, 147275, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='needs_ride_location',
            field=models.CharField(default='', max_length=200),
            preserve_default=True,
        ),
    ]
