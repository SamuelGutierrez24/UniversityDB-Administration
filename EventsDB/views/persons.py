from django.shortcuts import render
from pymongo import MongoClient


client = MongoClient("mongodb+srv://project:project@datos.ltwggtv.mongodb.net/?retryWrites=true&w=majority&appName=Datos")
db = client["Datos"]
personasdb = db["Personas"]
eventosdb = db["Eventos"]


def listP(request):
    personas = personasdb.find()
    context = {'personas': personas}
    return render(request,'persons.html', context)

def add_to_event(request):

    if request.method == 'POST':
        id = request.POST["identificacion"]
        persona = personasdb.find_one({"identificacion": id})
        
        eventos = eventosdb.find()
        context = {'persona': persona, 'eventos': eventos}
        return render(request,'add_to_event.html', context)