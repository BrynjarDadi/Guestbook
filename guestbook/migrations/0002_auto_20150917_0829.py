# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='question_text',
        ),
        migrations.AddField(
            model_name='text',
            name='guestbook_text',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='text',
            name='name',
            field=models.CharField(max_length=200, default=''),
        ),
    ]
