# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fun', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joke',
            name='name',
            field=models.CharField(max_length=b'30', null=True),
        ),
        migrations.AlterField(
            model_name='joke',
            name='tags',
            field=models.ManyToManyField(to='fun.Tag', null=True),
        ),
    ]
