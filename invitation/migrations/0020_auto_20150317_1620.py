# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0019_auto_20150317_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='group',
            field=models.CharField(choices=[('Bride Friends', 'Bride Friends'), ('Bride Family', 'Bride Family'), ('Groom Friends', 'Groom Friends'), ('Groom Family', 'Groom Family')], max_length=200, default='Bride Friends'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invitation',
            name='side',
            field=models.CharField(choices=[('Bride', 'Bride'), ('Groom', 'Groom'), ('Both', 'Both')], max_length=200, default='Both'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 3, 17, 14, 18, 58, 542353, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='invitation',
            name='personal_message',
            field=models.TextField(max_length=400, blank=True, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 3, 17, 14, 18, 58, 542353, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
