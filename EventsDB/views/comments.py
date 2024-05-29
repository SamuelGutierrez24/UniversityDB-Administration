from django.shortcuts import render
from pymongo import MongoClient
from EventsDB.forms import *

client = MongoClient("mongodb+srv://project:project@datos.ltwggtv.mongodb.net/?retryWrites=true&w=majority&appName=Datos")
db = client["Datos"]
comments_db = db["Comentarios"]

def filterComments(request):
    forms = CommentsForm(request.POST)

    if request.method == 'GET':
        ...
    context = {'form': forms}
    
    return render(request,'comments.html',context)