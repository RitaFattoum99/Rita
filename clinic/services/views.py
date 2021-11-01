from django.shortcuts import render
from .models import Patients

# Create your views here.


def index(request):
    patients = Patients.objects.all()
    return render(request, "services/index.html",{
       "patients" : patients 
    })

