# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fun', '0003_remove_joke_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joke',
            name='name',
            field=models.CharField(max_length=b'30', null=True, blank=True),
        ),
    ]
