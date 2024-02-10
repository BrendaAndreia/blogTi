# Generated by Django 5.0.1 on 2024-02-09 22:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogTi', '0022_remove_post_conteudo_remove_post_resumo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 9, 19, 20, 46, 263533)),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('post', models.ManyToManyField(to='blogTi.post')),
            ],
        ),
    ]
