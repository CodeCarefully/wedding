# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
import invitation.models


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0002_auto_20150327_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='invite_id',
            field=models.SlugField(default=invitation.models.id_generator, editable=False, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 27, 12, 26, 5, 874467, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 27, 12, 26, 5, 874467, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
    ]
