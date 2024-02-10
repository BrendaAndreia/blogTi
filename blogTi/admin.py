from django.contrib import admin
from .models import Post, Topico, Tag, Assunto,   Comentario, PostSituacao, Situacao


class TopicoInline(admin.TabularInline):
    model = Topico

class PostAdmin(admin.ModelAdmin):
    inlines = [
        TopicoInline
    ]
    class Meta:
        model = Post
        
        
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comentario)
admin.site.register(Assunto)
admin.site.register(PostSituacao)
admin.site.register(Situacao)
admin.site.register(Topico)
