# Generated by Django 5.0.1 on 2024-02-06 00:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogTi', '0005_alter_post_data_publicacao_alter_post_image_capa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 5, 21, 27, 36, 746631)),
        ),
    ]
