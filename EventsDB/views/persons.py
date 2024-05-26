from django.shortcuts import render

def listP(request):
    return render(request,'persons.html')

def add_to_event(request):
    return render(request,'add_to_event.html')