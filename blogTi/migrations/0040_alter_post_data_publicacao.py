# Generated by Django 5.0.1 on 2024-02-13 00:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogTi', '0039_alter_post_data_publicacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 12, 21, 42, 2, 905652)),
        ),
    ]
