# Generated by Django 5.0.1 on 2024-02-09 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contato', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='assunto',
            field=models.CharField(choices=[('', 'Selecione o assunto'), ('Dúvida', 'Dúvida'), ('Sugestão', 'Sugestão'), ('Reclamação', 'Reclamação'), ('Outros', 'Outros')], default='', max_length=100),
        ),
    ]
