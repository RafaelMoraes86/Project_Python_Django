from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Evento (models.Model) :
    titulo = models.CharField( max_length=100)
    descricao = models.TextField( blank= True, null= True)
    data_evento = models.DateTimeField( verbose_name='Data do Evento')
    data_descricao= models.DateTimeField( auto_now= True, verbose_name='Data de Criacao')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def data_event (self):
        return self.data_evento.strftime('%d/%m/%Y')

def str (self) :
    return self.titulo

    
   
