from django.shortcuts import redirect, render



from .models import Paciente



def index(request):
    return render(request, 'index.html',)
   
            

def cadastro(request):
    return render(request, 'cadastro.html',)


def questionario(request):
    return render(request, 'questionario.html',)
