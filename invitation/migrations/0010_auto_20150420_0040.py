# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0009_auto_20150418_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='family_rsvp_number',
            field=models.IntegerField(verbose_name='Number of people coming', default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 19, 21, 40, 55, 822311, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='diet_choices',
            field=models.CharField(blank=True, max_length=200, choices=[('Vegetarian', 'Vegetarian'), ('Vegan', 'Vegan'), ('Glatt Kosher', 'Glatt Kosher'), ('Other', 'Other')], verbose_name='Diet info'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 19, 21, 40, 55, 822311, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
    ]
