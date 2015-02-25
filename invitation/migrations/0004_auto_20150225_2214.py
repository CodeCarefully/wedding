# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0003_auto_20150225_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 25, 20, 14, 52, 127014, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='family_RSVP',
            field=models.CharField(max_length=200, default='Maybe'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='guest_RSVP',
            field=models.CharField(max_length=200, default='Maybe'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='with_guest',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.CharField(max_length=200, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='person_RSVP',
            field=models.CharField(max_length=200, default='Maybe'),
            preserve_default=True,
        ),
    ]
