from django.contrib import admin
from .models import Alternativa, Questao
# Register your models here.

class AlternativaInline(admin.TabularInline):
    model = Alternativa

class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AlternativaInline
    ]
    
    class Meta:
        model = Questao
        
        
admin.site.register(Alternativa)
admin.site.register(Questao, QuestionAdmin)