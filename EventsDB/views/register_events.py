import datetime
from django.shortcuts import render,redirect
from EventsDB.forms import *
from pymongo import MongoClient


client = MongoClient("mongodb+srv://project:project@datos.ltwggtv.mongodb.net/?retryWrites=true&w=majority&appName=Datos")
db = client["Datos"]
collection = db["Datos"]

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
            r_events_1 = request.session.get('r_events_1', {})
            r_events_2 = request.session.get('r_events_2', {})

            combined_data = {**r_events_1, **r_events_2}
            collection.insert_one(combined_data)
            print(request.POST)
            return redirect('menu')
    else:
        form = EventPlaceForm(request.POST)
        return render(request,'register_event_pagB.html',{'form': form})