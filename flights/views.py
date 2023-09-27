from django.shortcuts import render
from .models import Flight

def index(request):
    flights = Flight.objects.all()  # Query all flights from the database
    return render(request, "flights/index.html", {'flights': flights})

def flight_list(request):
    flights = Flight.objects.all()  # Query all flights from the database
    return render(request, 'flights/flight_list.html', {'flights': flights})
