# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-25 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='levelgradute',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Класс'),
        ),
        migrations.AlterField(
            model_name='task',
            name='difficult_level',
            field=models.IntegerField(choices=[(1, 'Прсотой'), (2, 'Средний'), (3, 'Сложный'), (4, 'Олимпиадный')], verbose_name='Уровень сложности'),
        ),
    ]
