# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import invitation.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0023_auto_20150318_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, default=1, auto_created=True, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='invite_id',
            field=models.IntegerField(default=invitation.models.id_generator, editable=False, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 3, 18, 20, 36, 14, 774219, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 3, 18, 20, 36, 14, 774219, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
