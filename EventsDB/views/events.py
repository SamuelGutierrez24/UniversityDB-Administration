from django.shortcuts import render
from bson.objectid import ObjectId
from pymongo import MongoClient
from EventsDB.forms import FilterEventsForm


client = MongoClient("mongodb+srv://project:project@datos.ltwggtv.mongodb.net/?retryWrites=true&w=majority&appName=Datos")
db = client["Datos"]
eventsdb = db["Eventos"]
personasdb = db["Personas"]


def listE(request):
    events = eventsdb.find()

    if request.method == 'GET':
       
        form = FilterEventsForm()
        context = {'events': events,
                'form':form}
        return render(request,'events.html', context)
    else:
        form = FilterEventsForm(request.POST)
        
        category = request.POST['categoria']
        print(category)
        events = eventsdb.find({'categoria':category})
        context = {'events': events,
                'form':form}
        return render(request,'events.html', context)
        

def show_event(request):
    if request.method == 'POST':
        titulo = request.POST["titulo"]
        event = eventsdb.find_one({"titulo": titulo})
        personas = event.get('personas', [])
        personas_ids = [(persona['identificacion']) for persona in personas]
        personas = []
        for persona_id in personas_ids:
            persona = personasdb.find_one({"identificacion": persona_id})
            if persona:
                personas.append(persona)
        
        context = {'event': event, 'personas' : personas}

        return render(request,'show_event.html', context)