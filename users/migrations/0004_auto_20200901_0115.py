# Generated by Django 3.1 on 2020-09-01 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200901_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='permissao',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='custom_user',
            name='telefone',
            field=models.CharField(default='1', max_length=50),
        ),
    ]
