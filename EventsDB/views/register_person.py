import datetime
from django.shortcuts import render,redirect
from EventsDB.forms import *
from pymongo import MongoClient


client = MongoClient("mongodb+srv://project:project@datos.ltwggtv.mongodb.net/?retryWrites=true&w=majority&appName=Datos")
db = client["Datos"]
personas = db["Personas"]

def register1(request):
    initial_data = request.session.get('pre_filled_data', {})
    form = UsuarioForm(initial=initial_data)
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            id = request.POST['identificacion']

            if personas.find_one({'identificacion':id}):
            
                form.add_error(None, 'El usuario ya existe.')
                return render(request, 'register_user.html', {'form': form})
            
            request.session['r_user_1'] = form.cleaned_data
            print(request.POST)
            return redirect('rUser_2')
    else:
        form = UsuarioForm(request.POST)
        return render(request,'register_user.html',{'form': form})
    
def register2(request):
    if request.method == 'POST':
        form = CityUserForm(request.POST)
        if form.is_valid():

            event_data = request.session.get('r_user_1', {})

            if personas.find_one({'identificacion':event_data['identificacion']}):
            
                form.add_error(None, 'El usuario ya existe.')
                return render(request, 'menu.html', {'form': form})
            
            request.session['r_user_2'] = form.cleaned_data
            r_user_1 = request.session.get('r_user_1', {})
            r_user_2 = request.session.get('r_user_2', {})
            combined_data = {**r_user_1, **r_user_2}
            personas.insert_one(combined_data)
            print(request.POST)
            return redirect('menu')
    else:
        form = CityUserForm(request.POST)
        return render(request,'register_user2.html',{'form': form})
    
    


