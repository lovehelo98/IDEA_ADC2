# Generated by Django 3.0.1 on 2020-01-11 14:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20200111_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 11, 20, 25, 9, 293644)),
        ),
        migrations.AlterField(
            model_name='message',
            name='message_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 11, 20, 25, 9, 293644)),
        ),
        migrations.AlterField(
            model_name='public',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 11, 20, 25, 9, 293644)),
        ),
    ]
