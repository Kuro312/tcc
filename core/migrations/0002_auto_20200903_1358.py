# Generated by Django 3.1 on 2020-09-03 16:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='turma',
            name='alunos',
            field=models.ManyToManyField(related_name='turma_alunos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='turma',
            name='vagas',
            field=models.IntegerField(default=10),
        ),
    ]
