# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0006_auto_20150411_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='group',
            field=models.CharField(choices=[('Friends', 'Friends'), ('Family', 'Family'), ('Work', 'Work'), ('Army', 'Army'), ("Siblings' friends", "Siblings' friends"), ("Parents' friends", "Parents' friends"), ('Family friends', 'Family friends'), ('Other', 'Other')], blank=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='language',
            field=models.CharField(choices=[('English', 'English'), ('Hebrew', 'Hebrew')], default='English', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 4, 11, 18, 27, 30, 190673, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 4, 11, 18, 27, 30, 190673, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
