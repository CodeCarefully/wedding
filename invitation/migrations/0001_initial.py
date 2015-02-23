# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('with_guest', models.BinaryField()),
                ('family_size', models.IntegerField(default=0)),
                ('guest_RSVP', models.IntegerField(default=2)),
                ('family_RSVP', models.IntegerField(default=2)),
                ('family_RSVP_number', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('person_RSVP', models.IntegerField(default=2)),
                ('invitation', models.ForeignKey(to='invitation.Invitation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
