# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_about_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=255)),
                ('slug', models.SlugField(unique=True, max_length=255)),
                ('content', redactor.fields.RedactorField(verbose_name='Text')),
                ('published', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='About',
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(help_text=b'Leave blank for auto-fill', max_length=255, null=True, blank=True),
        ),
    ]
