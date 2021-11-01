from django.shortcuts import render
from .models import Flight, Passengers
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def index(request):
    flights = Flight.objects.all()
    return render(request, "flights/index.html", {
        "flights": flights
    })


def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    passengers = flight.passengers.all()
    non_passengers = Passengers.objects.exclude(flights=flight).all()
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": passengers,
        "non_passengers": non_passengers
    })


def book(request, flight_id):
      if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)

        passenger_id = int(request.POST["passenger"])
        # this is the select name and he get value from
        # option which is passenger_id
        # we get the value as int because the default is get her as srting

        passenger = Passengers.objects.get(pk=passenger_id)
        # get the passenger by id

        passenger.flights.add(flight)
        # flights the variable which conect with Flight model ManyToMany

        return HttpResponseRedirect(reverse("flight", args=(flight_id, )))
        # flight is url name
        # we redirect page to flight page which we already inside her and
        # pass to her by args flight_id to keep us in same flight
        # we do this for refresh the page and add the new passengers
      return render(request, "flights/flight.html", {})
