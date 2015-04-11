# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import invitation.models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0005_auto_20150411_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='invite_id',
            field=models.SlugField(unique=True, editable=False, default=invitation.models.id_generator),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 11, 10, 14, 1, 567420, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 11, 10, 14, 1, 567420, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
    ]
