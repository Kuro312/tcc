# Generated by Django 3.1 on 2021-02-17 16:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20201212_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='data_nascimento',
            field=models.DateField(default=datetime.datetime(2021, 2, 17, 16, 42, 0, 839073, tzinfo=utc)),
        ),
    ]
