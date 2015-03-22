# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
import invitation.models


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0022_auto_20150317_2223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitation',
            name='id',
        ),
        migrations.AlterField(
            model_name='invitation',
            name='family_rsvp',
            field=models.CharField(max_length=200, choices=[('Yes', 'Yes'), ('Maybe', 'Maybe'), ('No', 'No')], default='Maybe'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='group',
            field=models.CharField(max_length=200, choices=[('Bride Friends', 'Bride Friends'), ('Bride Family', 'Bride Family'), ('Groom Friends', 'Groom Friends'), ('Groom Family', 'Groom Family')], blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='guest_rsvp',
            field=models.CharField(max_length=200, choices=[('Yes', 'Yes'), ('Maybe', 'Maybe'), ('No', 'No')], default='Maybe'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='invite_id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True, editable=False, default=invitation.models.id_generator),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 18, 20, 32, 51, 570202, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 18, 20, 32, 51, 570202, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='person_rsvp',
            field=models.CharField(max_length=200, choices=[('Yes', 'Yes'), ('Maybe', 'Maybe'), ('No', 'No')], default='Maybe'),
            preserve_default=True,
        ),
    ]
