from django.shortcuts import render
from pymongo import MongoClient
from EventsDB.forms import *

def filterComments(request):
    forms = CommentsForm(request.POST)
    context = {'form': forms}
    
    return render(request,'comments.html',context)