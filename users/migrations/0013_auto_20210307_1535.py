# Generated by Django 3.1 on 2021-03-07 18:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20210307_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='data_nascimento',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
