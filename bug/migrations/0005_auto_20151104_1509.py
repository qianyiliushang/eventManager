# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0004_remove_event_op_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='reporter',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
