from django.shortcuts import render
import datetime
# Create your views here.

app_name = "tasks"

def index(request):
    now = datetime.datetime.now()
    return render (request, "tasks/index.html",{
        "now" : now
    })