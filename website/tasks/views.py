from django.shortcuts import render
from django import forms
import datetime
# Create your views here.

app_name = "tasks"

tasks = ["Check Email", "Make Files", "Run As Administartor"]

def index(request):
    now = datetime.datetime.now()
    return render (request, "tasks/index.html",{
        "now" : now
    })

def add(request):
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })

class NewTaskForm(forms.Form):
    task = forms.CharField(label="Add Task")