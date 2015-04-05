# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='propertyType',
            field=models.CharField(max_length=1, choices=[(b'h', b'House'), (b'a', b'Apartment')]),
        ),
    ]
