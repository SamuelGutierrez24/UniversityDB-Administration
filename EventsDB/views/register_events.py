import datetime
from django.shortcuts import render,redirect
from EventsDB.forms import *
from pymongo import MongoClient


client = MongoClient("mongodb+srv://project:project@datos.ltwggtv.mongodb.net/?retryWrites=true&w=majority&appName=Datos")
db = client["Datos"]
eventos = db["Eventos"]
lugares = db["Lugares"]

def register1(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            fecha = datetime.datetime.strptime(request.POST['fecha'], '%Y-%m-%d').date()
            fecha2 = fecha.isoformat()
            titulo = request.POST['titulo']

            if eventos.find_one({'titulo': titulo, 'fecha': fecha2}):
            
                form.add_error(None, 'El evento con este título y fecha ya existe.')
                return render(request, 'register_event_pageA.html', {'form': form})
            
            facultades_seleccionadas = form.cleaned_data['facultad']
            nombres_facultades = [facultad.nombre for facultad in facultades_seleccionadas]
            request.session['r_events_1'] = {
                'titulo': form.cleaned_data['titulo'],
                'descripcion': form.cleaned_data['descripcion'],
                'categoria': form.cleaned_data['categoria'],
                'fecha': fecha2,
                'facultad': nombres_facultades
            }
            print(request.session['r_events_1'])
            print(request.POST)
            print('antes')
            return redirect('rEvents_b')
        else:
            return render(request, 'register_event_pageA.html', {'form': form})
    
    else:
        form = EventForm()
        print(form)
        return render(request,'register_event_pageA.html',{'form': form})
    
def register2(request):
    if request.method == 'POST':
        form = EventPlaceForm(request.POST)
        if form.is_valid():
            
            event_data = request.session.get('r_events_1', {})
            if eventos.find_one({'titulo': event_data['titulo'], 'fecha': event_data['fecha']}):
                return render(request, 'menu.html', {'form': form})
            
            request.session['r_events_2'] = form.cleaned_data
            r_events_1 = request.session.get('r_events_1', {})
            r_events_2 = request.session.get('r_events_2', {})
            lugar = {**r_events_2}

            lugar_id = lugares.insert_one(lugar).inserted_id
            evento = {**r_events_1,'lugar': { '_id':lugar_id,**r_events_2}}
            eventos.insert_one(evento)
            
            print(request.POST)
            return redirect('menu')
    else:
        print('llegue')
        form = EventPlaceForm(request.POST)
        return render(request,'register_event_pagB.html',{'form': form})