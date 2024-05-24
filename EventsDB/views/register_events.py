import datetime
from django.shortcuts import render,redirect
from EventsDB.forms import *

def register1(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            fecha = datetime.datetime.strptime(request.POST['fecha'], '%Y-%m-%d').date()
            fecha2 = fecha.isoformat()
            request.session['r_events_1'] = {
                'titulo': request.POST['titulo'],
                'descripcion': request.POST['descripcion'],
                'categoria': request.POST['categoria'],
                'fecha': fecha2
            }
            print(request.POST)
            return redirect('rEvents_b')
        else:
            # Form is not valid, re-render the form with validation errors
            return render(request, 'register_event_pageA.html', {'form': form})
    
    else:
        form = EventForm(request.POST)
        return render(request,'register_event_pageA.html',{'form': form})
    
def register2(request):
    if request.method == 'POST':
        form = EventPlaceForm(request.POST)
        if form.is_valid():
            request.session['r_events_2'] = form.cleaned_data
            print(request.POST)
    else:
        form = EventPlaceForm(request.POST)
        return render(request,'register_event_pagB.html',{'form': form})
    


