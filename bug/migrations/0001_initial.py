# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name=b'\xe6\x8f\x90\xe4\xba\xa4\xe6\x97\xb6\xe9\x97\xb4', auto_created=True)),
                ('title', models.CharField(max_length=120, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('content', models.TextField(verbose_name=b'\xe9\x97\xae\xe9\xa2\x98\xe8\xaf\xa6\xe6\x83\x85')),
                ('version', models.FloatField(verbose_name=b'\xe7\x89\x88\xe6\x9c\xac')),
                ('business_type', models.CharField(max_length=120, verbose_name=b'\xe4\xb8\x9a\xe5\x8a\xa1\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(b'student', b'\xe5\xae\xb6\xe9\x95\xbf\xe7\xab\xaf'), (b'teacher', b'\xe8\x80\x81\xe5\xb8\x88\xe7\xab\xaf'), (b'admin', b'\xe8\xbf\x90\xe8\x90\xa5\xe7\xab\xaf'), (b'ta', b'\xe5\x8a\xa9\xe6\x95\x99\xe7\xab\xaf'), (b'third_place', b'\xe7\xac\xac\xe4\xb8\x89\xe6\x96\xb9\xe5\x9c\xba\xe5\x9c\xb0')])),
                ('platform', models.CharField(max_length=120, verbose_name=b'\xe5\xae\xa2\xe6\x88\xb7\xe7\xab\xaf', choices=[(b'ios', b'IOS'), (b'android', b'\xe5\xae\x89\xe5\x8d\x93'), (b'web', b'WEB')])),
                ('status', models.CharField(max_length=120, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(b'create', b'\xe6\x96\xb0\xe5\xbb\xba'), (b'review', b'\xe5\xae\xa1\xe6\xa0\xb8'), (b'assigned', b'\xe5\xb7\xb2\xe5\x88\x86\xe6\xb4\xbe(\xe6\x8a\x80\xe6\x9c\xaf\xe9\x83\xa8)'), (b'resolved', b'\xe5\xb7\xb2\xe8\xa7\xa3\xe5\x86\xb3'), (b'closed', b'\xe5\x85\xb3\xe9\x97\xad'), (b'duplicated', b'\xe9\x87\x8d\xe5\xa4\x8d\xe7\x9a\x84')])),
                ('comments', models.TextField(verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
                ('last_update_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x9c\x80\xe5\x90\x8e\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('level', models.CharField(max_length=100, verbose_name=b'\xe4\xb8\xa5\xe9\x87\x8d\xe7\xad\x89\xe7\xba\xa7')),
                ('solution', models.CharField(max_length=100, verbose_name=b'\xe8\xa7\xa3\xe5\x86\xb3\xe6\x96\xb9\xe6\xa1\x88')),
                ('emergency', models.CharField(max_length=100, verbose_name=b'\xe7\xb4\xa7\xe6\x80\xa5\xe7\xa8\x8b\xe5\xba\xa6')),
                ('channel', models.CharField(max_length=100, verbose_name=b'\xe6\x9d\xa5\xe6\xba\x90', blank=True)),
                ('attachment', models.FileField(upload_to=b'E:\\pythonproject\\OnlineBug\\static\\media_root', verbose_name=b'\xe9\x99\x84\xe4\xbb\xb6')),
            ],
        ),
        migrations.CreateModel(
            name='EventLog',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('event_id', models.IntegerField(verbose_name=b'\xe9\x97\xae\xe9\xa2\x98\xe7\xbc\x96\xe5\x8f\xb7')),
                ('operation', models.CharField(max_length=120, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c')),
                ('op_time', models.DateTimeField(auto_now_add=True)),
                ('op_user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='op_history',
            field=models.ForeignKey(to='bug.EventLog'),
        ),
        migrations.AddField(
            model_name='event',
            name='reporter',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
