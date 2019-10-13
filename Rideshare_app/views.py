from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Ride, Rider, Driver
from django.urls import reverse
from django.views import generic

def index(request):
    return HttpResponse("Hello, world. You're at the RideShare index.")

def search(request):
	return render(request, 'Rideshare_app/search.html')

def login(request):
	return HttpResponse("Display login!")

def rider_profile(request, rider_id):
    rider = get_object_or_404(Rider, pk = rider_id)
    ride = Ride.objects.get(pk= rider.ride.id)
    context = {"rider" : rider, "ride" : ride}
    return render(request, 'Rideshare_app/rider_profile.html', context)

def driver_profile(request, driver_id):
    driver = get_object_or_404(Driver, pk = driver_id)
    ride = Ride.objects.get(pk= driver.ride.id)
    context = {"driver" : driver, "ride" : ride}
    return render(request, 'Rideshare_app/driver_profile.html', context)

def ride(request, id):
    ride = get_object_or_404(Ride, pk = id)
    context = {"ride" : ride}
    return render(request, 'Rideshare_app/ride.html', context)
