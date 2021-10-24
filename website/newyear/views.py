from django.shortcuts import render
from . import views
import datetime
# Create your views here.

app_name = "newyear"

def index(request):
    return render (request, "newyear/index.html", {
        "now" : datetime.datetime.now()
    })
