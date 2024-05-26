from django.shortcuts import render
from pymongo import MongoClient


client = MongoClient("mongodb+srv://project:project@datos.ltwggtv.mongodb.net/?retryWrites=true&w=majority&appName=Datos")
db = client["Datos"]
eventsdb = db["Eventos"]


def listE(request):
    events = eventsdb.find()
    context = {'events': events}
    return render(request,'events.html', context)