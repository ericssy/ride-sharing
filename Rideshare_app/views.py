from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Ride, Rider, Driver
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic.list import ListView

def index(request):
    return render(request, 'Rideshare_app/homepage.html')

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


class RidesListView(generic.ListView):
    template_name = 'Rideshare_app/upcoming_rides_list.html'
    context_object_name = 'upcoming_rides_list'
    paginate_by = 10

    def get_queryset(self):
        # return all the upcoming trips
        return Ride.objects.filter(date__gte = timezone.now(), driver__isnull = False)
