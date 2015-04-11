# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0007_auto_20150411_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='is_family',
            field=models.BooleanField(default=False, verbose_name='Check for family invitation'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 4, 11, 18, 40, 45, 452938, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='with_guest',
            field=models.BooleanField(default=False, verbose_name='Invite a +1 with guest'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='diet_blank',
            field=models.CharField(blank=True, max_length=200, default='', verbose_name='Other diet info'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='diet_choices',
            field=models.CharField(blank=True, max_length=200, choices=[('Vegetarian', 'Vegetarian'), ('Vegan', 'Vegan'), ('Allergies', 'Allergies'), ('Glatt Kosher', 'Glatt Kosher')], verbose_name='Diet info'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 4, 11, 18, 40, 45, 452938, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
