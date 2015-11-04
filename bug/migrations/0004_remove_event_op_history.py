# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0003_auto_20151104_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='op_history',
        ),
    ]
