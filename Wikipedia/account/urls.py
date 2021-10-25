from django.urls import path
from . import views 

app_name = "account"

urlpatterns =[
    path("", views.index, name="index"),
    path("creat", views.creat, name="creat"),
]