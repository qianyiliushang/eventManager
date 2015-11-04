# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0002_auto_20151103_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attachment',
            field=models.FileField(upload_to=b'E:\\pythonproject\\OnlineBug\\static\\media_root', verbose_name=b'\xe9\x99\x84\xe4\xbb\xb6'),
        ),
    ]
