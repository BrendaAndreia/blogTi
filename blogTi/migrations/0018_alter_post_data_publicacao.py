# Generated by Django 5.0.1 on 2024-02-09 19:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogTi', '0017_alter_post_data_publicacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 9, 16, 7, 29, 442471)),
        ),
    ]
