# Generated by Django 3.1 on 2020-09-01 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='permissao',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='custom_user',
            name='telefone',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
