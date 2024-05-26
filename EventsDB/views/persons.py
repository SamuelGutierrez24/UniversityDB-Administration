from django.shortcuts import render
from pymongo import MongoClient


client = MongoClient("mongodb+srv://project:project@datos.ltwggtv.mongodb.net/?retryWrites=true&w=majority&appName=Datos")
db = client["Datos"]
personasdb = db["Personas"]


def listP(request):

    personas = personasdb.find()
    context = {'personas': personas}

    if request.method == 'GET':
        return render(request,'persons.html', context)
    else:
        if 'searchBtn' in request.POST:
            if 'idPerson' != None:
                id = request.POST.get('idPerson')
            
                personas = personasdb.find({'identificacion':id})

        context = {'personas': personas}

        return render(request,'persons.html', context)


    



def add_to_event(request):
    return render(request,'add_to_event.html')