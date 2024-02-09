from django.db import models
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

class Post(models.Model):
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    resumo = RichTextField(blank=True, null=True)
    conteudo = RichTextUploadingField()
    image_capa = models.ImageField(upload_to='static/blog/%Y/%m/%d/', blank=True, null=True)
    data_publicacao = models.DateTimeField(default=datetime.now())


    def __str__(self):
        return self.titulo
    