from django.contrib import admin
from .models import Post, Topico, Tag, Assunto,   Comentario, PostSituacao, Situacao


class TopicoInline(admin.TabularInline):
    model = Topico
    extra = 1

class TagInline(admin.TabularInline):
    model = Tag.post.through
    extra = 1


class AssuntoInline(admin.TabularInline):
    model = Assunto.post.through
    extra = 1


class SituacaoInline(admin.TabularInline):
    model = PostSituacao
    extra = 1


class SituacaoAdmin(admin.ModelAdmin):
    inlines = [
        SituacaoInline
    ]

class PostAdmin(admin.ModelAdmin):
    inlines = [
        TopicoInline,
        TagInline,
        AssuntoInline,
        SituacaoInline,
    ]
    class Meta:
        model = Post
       
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comentario)
admin.site.register(Assunto)
admin.site.register(PostSituacao)
admin.site.register(Situacao, SituacaoAdmin)
admin.site.register(Topico)
