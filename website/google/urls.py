from django.urls import path
from . import views 

urlpatterns =[
    path("", views.index, name="index"),
    # path("<str:name>", views.greet, name="greet"),
    path("<int:birth>", views.birth, name="birth"),
    # path("christmas",views.christmas, name="christmas")
]