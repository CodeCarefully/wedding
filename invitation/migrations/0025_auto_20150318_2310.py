# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import invitation.models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0024_auto_20150318_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='invite_id',
            field=models.SlugField(default=invitation.models.id_generator, unique=True, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 3, 18, 21, 10, 16, 707974, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 3, 18, 21, 10, 16, 707974, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
