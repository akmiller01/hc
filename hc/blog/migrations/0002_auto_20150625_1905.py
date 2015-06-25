# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('slug', models.SlugField(unique=True, max_length=255)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=redactor.fields.RedactorField(verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='tag',
            name='post',
            field=models.ForeignKey(related_query_name=b'tag', related_name='tags', to='blog.Post'),
        ),
    ]
