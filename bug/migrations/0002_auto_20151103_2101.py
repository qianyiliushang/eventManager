# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attachment',
            field=models.FileField(upload_to=b'/Users/zombie/git/eventManager/static/media_root', verbose_name=b'\xe9\x99\x84\xe4\xbb\xb6'),
        ),
    ]
