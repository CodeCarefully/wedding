# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0017_auto_20150315_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='email',
        ),
        migrations.AddField(
            model_name='person',
            name='email_app',
            field=models.EmailField(blank=True, default='', max_length=75),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='email_internal_use',
            field=models.EmailField(blank=True, default='', max_length=75),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='phone_app',
            field=models.CharField(blank=True, default='', max_length=15),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 3, 17, 13, 51, 43, 17680, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 3, 17, 13, 51, 43, 17680, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
