# Generated by Django 5.0.1 on 2024-02-09 22:46

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogTi', '0029_alter_post_data_publicacao_delete_comentario'),
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 9, 19, 46, 50, 815323)),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(max_length=1024)),
                ('perfil', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contas.perfil')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogTi.post')),
            ],
        ),
    ]
