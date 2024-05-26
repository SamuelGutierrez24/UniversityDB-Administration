from django.shortcuts import render,redirect
from EventsDB.forms import *
from pymongo import MongoClient

client = MongoClient("mongodb+srv://project:project@datos.ltwggtv.mongodb.net/?retryWrites=true&w=majority&appName=Datos")
db = client["Datos"]
eventos = db["Eventos"]

def filter_Event(request):

  
    
    if request.method == 'GET':
        return render(request,'filter_event.html',{
            'form' : FilterEventForm,
            'error': "Error en la conexión",
            'events' : eventos.find()
        })
    else:
        if 'searchBtn' in request.POST:
            form = FilterEventForm(request.POST)
            if(form.is_valid()):
                titulo = request.POST['titulo']

                events =  eventos.find({'titulo': titulo})

        return render(request,'filter_event.html',{
            'form' : FilterEventForm,
            'error': "Error en la conexión",
            'events' : events
        })