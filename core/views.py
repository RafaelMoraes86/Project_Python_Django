from django.shortcuts import render
from core.models import Evento

# Create your views here.

def listaEventos(request) :
    evento = Evento.objects.all()
    dados ={'eventos': evento}
    return render(request, 'index.html', dados)
