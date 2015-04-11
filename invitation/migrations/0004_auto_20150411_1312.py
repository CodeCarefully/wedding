# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0003_auto_20150411_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='date_opened',
            field=models.DateTimeField(default=datetime.datetime(2000, 1, 1, 0, 0)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invitation',
            name='family_rsvp',
            field=models.CharField(default='Maybe', choices=[('Yes', 'Yes'), ('Maybe', 'Maybe'), ('No', 'No')], max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invitation',
            name='family_rsvp_number',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invitation',
            name='family_size',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invitation',
            name='group',
            field=models.CharField(default='', choices=[('Friends', 'Friends'), ('Family', 'Family'), ('Work', 'Work'), ('School', 'School'), ('Army', 'Army'), ("Siblings' friends", "Siblings' friends"), ("Parents' friends", "Parents' friends"), ('Family friends', 'Family friends'), ("Grandparents' friends", "Grandparents' friends"), ('Other', 'Other')], blank=True, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invitation',
            name='invitation_name',
            field=models.CharField(default='', blank=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invitation',
            name='is_family',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invitation',
            name='language',
            field=models.CharField(default='English', choices=[('English', 'English'), ('Hebrew', 'Hebrew')], blank=True, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invitation',
            name='side',
            field=models.CharField(default='Both', choices=[('Bride', 'Bride'), ('Groom', 'Groom'), ('Both', 'Both')], max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invitation',
            name='was_opened',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 11, 10, 12, 36, 667459, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='with_guest',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
