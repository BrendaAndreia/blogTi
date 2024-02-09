from django.db import models

CHOICES_ASSUNTOS =[
    ('', 'Selecione o assunto'),
    ('Dúvida', 'Dúvida'),
    ('Sugestão', 'Sugestão'),
    ('Reclamação', 'Reclamação'),
    ('Outros', 'Outros'),
]
# Create your models here.
class Contato(models.Model):
    assunto = models.CharField(choices=CHOICES_ASSUNTOS, default="",max_length=100)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mensagem = models.TextField(max_length=1000)