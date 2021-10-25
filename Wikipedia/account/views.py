from collections import namedtuple
from django.shortcuts import render
from django import forms

# Create your views here.

def index (request):
    return render (request, "account/index.html", {
    #    "account": request.sesion["account"]
    })

def creat(request):
    if request.method == "POST":
        form = CreateAccount(request.POST)

        if form.is_valid():
            
            name = form.cleaned_data["name"]

            # request.session["account"] += form
        else:
            return render(request, "account/index.html", {
                "form": form
            })
        
   
    return render (request, "account/index.html",{
        "form": CreateAccount()
    })

class CreateAccount(forms.Form):
    name = forms.CharField(label="Your Name")
    # password = forms.CharField(label="password" ,widget=forms.PasswordInput)
