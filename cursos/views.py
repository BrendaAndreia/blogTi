from django.shortcuts import render

# Create your views here.
def cursos(request):
    return render(request, 'cursos/cursos.html')