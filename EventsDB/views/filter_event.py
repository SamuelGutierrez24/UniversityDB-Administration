from django.shortcuts import render,redirect
from EventsDB.forms import *

def filter_Event(request):
    return render(request,'filter_event.html')