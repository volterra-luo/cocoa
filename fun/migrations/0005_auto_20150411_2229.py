# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fun', '0004_auto_20150411_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joke',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 4, 11, 14, 29, 47, 290000, tzinfo=utc), max_length=b'30', blank=True),
            preserve_default=False,
        ),
    ]
