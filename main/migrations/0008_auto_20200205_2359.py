# Generated by Django 3.0.1 on 2020-02-05 18:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200205_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 23, 59, 2, 498478)),
        ),
        migrations.AlterField(
            model_name='message',
            name='message_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 23, 59, 2, 506456)),
        ),
        migrations.AlterField(
            model_name='public',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 23, 59, 2, 504683)),
        ),
    ]
