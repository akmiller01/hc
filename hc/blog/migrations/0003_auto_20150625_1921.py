# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150625_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ForeignKey(related_query_name=b'post', related_name='posts', blank=True, to='blog.Tag', null=True),
        ),
    ]
