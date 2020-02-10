# Generated by Django 3.0.1 on 2020-02-09 09:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideapeacher', '0002_auto_20200208_0130'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='pdf',
            field=models.FileField(blank=True, upload_to='idea/pdfs'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 9, 15, 14, 20, 801672)),
        ),
        migrations.AlterField(
            model_name='message',
            name='message_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 9, 15, 14, 20, 803666)),
        ),
        migrations.AlterField(
            model_name='public',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 9, 15, 14, 20, 802670)),
        ),
    ]
