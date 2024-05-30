from django.shortcuts import render
from pymongo import MongoClient


client = MongoClient("mongodb+srv://project:project@datos.ltwggtv.mongodb.net/?retryWrites=true&w=majority&appName=Datos")
db = client["Datos"]
personasdb = db["Personas"]
eventosdb = db["Eventos"]


def listP(request):
    personas = personasdb.find()
    context = {'personas': personas}

    if request.method == 'GET':
        return render(request,'persons.html', context)
    else:
        peopleID = personasdb.find()
        if 'searchBtn' in request.POST:
            if request.POST['idPerson'] == 'Empty':
                peopleID = personasdb.find()
            id = request.POST['idPerson']
            peopleID = personasdb.find({'identificacion': f'{id}'})
            print(type(id))
        context = {'personas': peopleID}
        return render(request,'persons.html', context)


def add_to_event(request):

    if request.method == 'POST':
        id = request.POST["identificacion"]
        request.session['persona_id'] = id
        persona = personasdb.find_one({"identificacion": id})
        eventos = eventosdb.find()
        print(eventos)
        context = {'persona': persona, 'eventos': eventos}
        return render(request,'add_to_event.html', context)
    
    elif request.method == 'GET':
        titulo = request.GET.get("tituloEvento")
        print(f"eventoId recibido: {titulo}")
        personaId = request.session.get('persona_id')
        print(titulo)
        persona = personasdb.find_one({"identificacion": personaId})
        eventosdb.update_one({"titulo" : titulo},{"$push": {"personas": persona}})
        return render(request,'menu.html')
    else:
        return render(request,'persons.html', context)