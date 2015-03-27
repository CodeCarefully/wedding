# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import invitation.models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('modified_date', models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 3, 27, 12, 16, 35, 544793, tzinfo=utc))),
                ('invite_id', models.SlugField(unique=True, editable=False, default=invitation.models.id_generator)),
                ('with_guest', models.BooleanField(default=False)),
                ('family_size', models.IntegerField(default=0)),
                ('family_rsvp', models.CharField(max_length=200, choices=[('Yes', 'Yes'), ('Maybe', 'Maybe'), ('No', 'No')], default='Maybe')),
                ('family_rsvp_number', models.IntegerField(default=0)),
                ('personal_message', models.TextField(max_length=400, default='', blank=True)),
                ('invitation_name', models.CharField(max_length=200, default='', blank=True)),
                ('date_opened', models.DateTimeField(default=datetime.datetime(2000, 1, 1, 0, 0))),
                ('was_opened', models.BooleanField(default=False)),
                ('side', models.CharField(max_length=200, choices=[('Bride', 'Bride'), ('Groom', 'Groom'), ('Both', 'Both')], default='Both')),
                ('group', models.CharField(max_length=200, choices=[('Friends', 'Friends'), ('Family', 'Family'), ('Work', 'Work'), ('School', 'School'), ('Other', 'Other')], blank=True)),
                ('couple', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('modified_date', models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 3, 27, 12, 16, 35, 544793, tzinfo=utc))),
                ('name', models.CharField(max_length=200, default='')),
                ('email_internal_use', models.EmailField(max_length=75, default='', blank=True)),
                ('person_rsvp', models.CharField(max_length=200, choices=[('Yes', 'Yes'), ('Maybe', 'Maybe'), ('No', 'No')], default='Maybe')),
                ('is_vegan', models.BooleanField(default=False)),
                ('diet_info', models.CharField(max_length=200, default='', blank=True)),
                ('needs_ride_location', models.CharField(max_length=200, default='', blank=True)),
                ('has_car_room_location', models.CharField(max_length=200, default='', blank=True)),
                ('number_of_seats', models.IntegerField(default=0)),
                ('email_app', models.EmailField(max_length=75, default='', blank=True)),
                ('phone_app', models.CharField(max_length=15, default='', blank=True)),
                ('invitation', models.ForeignKey(to='invitation.Invitation')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
