from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogTi.urls')), 
    path('login/', include('autenticacao.urls')),
    path('cursos/', include('cursos.urls')),
    path('contato/', include('contato.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),#rotas, link etc
    path('contas/', include('contas.urls')),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
