# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DRCA', '0002_curso_tipo_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='tipo_curso',
            field=models.CharField(max_length=11),
            preserve_default=True,
        ),
    ]
