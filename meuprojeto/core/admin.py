from django.contrib import admin
from core.models import Evento



class EventoAdmin(admin.ModelAdmin) :
    list_display = ('titulo', 'data_evento', 'data_descricao')
    list_filter = ('usuario', 'data_evento',)

# Register your models here.
admin.site.register(Evento, EventoAdmin)