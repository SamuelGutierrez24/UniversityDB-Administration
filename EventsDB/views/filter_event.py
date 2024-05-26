from django.shortcuts import render,redirect
from EventsDB.forms import *

def filter_Event(request):

    if request.method == 'GET':
        return render(request,'filter_event.html',{
            'form' : FilterEventForm,
            'error': "Error en la conexión"
        })
    else:
        if 'searchBtn' in request.POST:
            ...