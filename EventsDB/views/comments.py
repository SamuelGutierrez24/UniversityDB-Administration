from django.shortcuts import render
from pymongo import MongoClient
from EventsDB.forms import *

client = MongoClient("mongodb+srv://project:project@datos.ltwggtv.mongodb.net/?retryWrites=true&w=majority&appName=Datos")
db = client["Datos"]
comments_db = db["Comentarios"]
personas = db["Personas"]
eventsdb = db["Eventos"]

def filterComments(request):
    forms = CommentsForm(request.POST)
    comments_info = comments_db.find()
    context = {'form': forms,
            'comments': comments_info}

    if request.method == 'GET':
        context = {'form': forms,
                   'comments': comments_info}
        return render(request,'comments.html',context)
    else:
        if forms.is_valid():
            idPerson = request.POST['idPerson']

            if personas.find({'identificacion':idPerson}) is False:
                forms.add_error(None, 'El usuario no existe.')
                return render(request,'comments.html',context)
            
            idEvent = request.POST['idEvent']

            if eventsdb.find({'titulo':idEvent}) is False:
                forms.add_error(None, 'El usuario no existe.')
                return render(request,'comments.html',context)
            
            request.session['r_comment'] = forms.cleaned_data

            comments = request.session.get('r_comment',{})


            comments_db.insert_one({**comments})
            print(request.POST)
            
    