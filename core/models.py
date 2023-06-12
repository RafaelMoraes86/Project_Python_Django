from django.db import models

# Create your models here.
class Event (models.Model) :
    title = models.CharField( max_length=100)
    descrition = models.TextField( blank= True, null= True)
    date_event = models.DateTimeField()
    date_criation = models.DateTimeField(auto_now=True)


   
