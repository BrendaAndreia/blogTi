# Generated by Django 5.0.1 on 2024-02-09 23:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogTi', '0032_alter_post_data_publicacao_postsituacao_situacao_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='situacao',
            name='posts',
        ),
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 9, 20, 40, 37, 160804)),
        ),
        migrations.DeleteModel(
            name='PostSituacao',
        ),
        migrations.DeleteModel(
            name='Situacao',
        ),
    ]
