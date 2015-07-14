# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20150714_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='subtitle',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
