# Generated by Django 4.0.3 on 2022-05-31 17:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('RESTApi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 17, 15, 23, 339298, tzinfo=utc)),
        ),
    ]
