# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0004_auto_20150411_1312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('modified_date', models.DateTimeField(default=datetime.datetime(2015, 4, 11, 10, 13, 34, 961142, tzinfo=utc), auto_now=True)),
                ('english_name', models.CharField(max_length=200, default='')),
                ('hebrew_name', models.CharField(max_length=200, default='')),
                ('email', models.EmailField(max_length=75, default='', blank=True)),
                ('person_rsvp', models.CharField(max_length=200, choices=[('Yes', 'Yes'), ('Maybe', 'Maybe'), ('No', 'No')], default='Maybe')),
                ('diet_choices', models.CharField(max_length=200, choices=[('Vegetarian', 'Vegetarian'), ('Vegan', 'Vegan'), ('Allergies', 'Allergies'), ('Glatt Kosher', 'Glatt Kosher')], blank=True)),
                ('diet_blank', models.CharField(max_length=200, default='', blank=True)),
                ('invitation', models.ForeignKey(to='invitation.Invitation')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 11, 10, 13, 34, 961142, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
    ]
