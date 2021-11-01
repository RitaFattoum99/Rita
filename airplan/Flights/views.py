from django.shortcuts import render
from .models import  Flight , Passengers
# Create your views here.

def index (request):
    return render (request, "flights/index.html", {
        
    })