# Generated by Django 3.0.2 on 2020-02-04 18:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200204_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 0, 3, 26, 598262)),
        ),
        migrations.AlterField(
            model_name='message',
            name='message_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 0, 3, 26, 602251)),
        ),
        migrations.AlterField(
            model_name='public',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 5, 0, 3, 26, 601254)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(blank=True),
        ),
    ]
