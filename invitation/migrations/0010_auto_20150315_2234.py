# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
import invitation.models


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0009_auto_20150314_2012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='name',
        ),
        migrations.AddField(
            model_name='invitation',
            name='invitation_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invitation',
            name='invite_id',
            field=models.IntegerField(default=invitation.models.id_generator, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='english_name',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='hebrew_name',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='family_RSVP',
            field=models.CharField(default='Maybe', max_length=200, choices=[('yes', 'yes'), ('Maybe', 'Maybe'), ('No', 'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='guest_RSVP',
            field=models.CharField(default='Maybe', max_length=200, choices=[('yes', 'yes'), ('Maybe', 'Maybe'), ('No', 'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 15, 20, 34, 33, 406014, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 15, 20, 34, 33, 406014, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='person_RSVP',
            field=models.CharField(default='Maybe', max_length=200, choices=[('yes', 'yes'), ('Maybe', 'Maybe'), ('No', 'No')]),
            preserve_default=True,
        ),
    ]
