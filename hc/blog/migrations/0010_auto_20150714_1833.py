# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_page_subtitle'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='page',
            name='order',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
