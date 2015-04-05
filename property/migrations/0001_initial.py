# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.DecimalField(max_digits=16, decimal_places=2)),
                ('price', models.DecimalField(max_digits=16, decimal_places=2)),
                ('sqrPrice', models.DecimalField(max_digits=16, decimal_places=2)),
                ('propertyType', models.TextField()),
                ('listingType', models.TextField()),
                ('numberOfRooms', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('mainTitle', models.TextField()),
                ('status', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(related_name=b'snippets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
    ]
