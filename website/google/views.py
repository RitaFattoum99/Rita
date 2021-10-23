from django.http.response import HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.

def index(request):
    return HttpResponse("Hello World!")

# def greet(request ,name):
#     return HttpResponse(f"Hello, {name}!".title())

def greet(request, name):
    return render (request, 'hello/index.html', {
        "name" : name.title()
    })

# def christmas(request):
#     now = datetime.datetime.now()
#     return render(request, 'hello/index.html', {
#         "christmas" : now.month == 1 and now.day == 1 
#     })    

def birth(request, birth):
    today = datetime.datetime.now()
    return render(request, 'hello/index.html' ,{
        "age" : today.year - birth
    })