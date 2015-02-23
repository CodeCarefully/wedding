# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='with_guest',
            field=models.BinaryField(),
            preserve_default=True,
        ),
    ]
