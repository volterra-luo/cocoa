# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fun', '0002_auto_20150411_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joke',
            name='tags',
        ),
    ]
