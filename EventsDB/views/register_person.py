import datetime
from django.shortcuts import render,redirect
from EventsDB.forms import *

def register1(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
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
            request.session['r_user_2'] = form.cleaned_data
            print(request.POST)
    else:
        form = CityUserForm(request.POST)
        return render(request,'register_user2.html',{'form': form})
    


