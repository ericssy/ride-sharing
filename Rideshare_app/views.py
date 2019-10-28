from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Ride, Rider, Driver
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic.list import ListView
from .forms import PostRideAsDriverForm
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return render(request, 'Rideshare_app/homepage.html')

def search(request):
	return render(request, 'Rideshare_app/search.html')

def login(request):
	return HttpResponse("Display login!")

def rider_profile(request, rider_id):
    rider = get_object_or_404(Rider, pk = rider_id)
    context = {"rider" : rider, "ride" : ride}
    return render(request, 'Rideshare_app/rider_profile.html', context)

def driver_profile(request, driver_id):
    driver = get_object_or_404(Driver, pk = driver_id)
    upcoming_rides_list = Ride.objects.filter(driver = driver_id, date__gte = timezone.now())
    past_rides = Ride.objects.filter(driver = driver_id, date__lt = timezone.now())
    context = {"driver" : driver, "upcoming_rides_list" : upcoming_rides_list,
                "past_rides" : past_rides}
    return render(request, 'Rideshare_app/driver_profile.html', context)

def ride(request, id):
    ride = get_object_or_404(Ride, pk = id)
    context = {"ride" : ride}
    return render(request, 'Rideshare_app/ride.html', context)

def post_ride_driver(request, driver_id):
    driver = get_object_or_404(Driver, pk = driver_id)
    context = {"driver" : driver}
    if request.method == "POST":
        form = PostRideAsDriverForm(request.POST)
        if form.is_valid() == True:
            departure_location = form.cleaned_data["departure_location"]
            date = form.cleaned_data["date"]
            destination_location = form.cleaned_data["destination_location"]
            Ride.objects.create(date = date, driver = driver, departure_location = departure_location, destination_location = destination_location)
            return HttpResponseRedirect(reverse('post_ride_driver_result', args=(driver_id,)))
            #return render(request, 'Rideshare_app/post_ride_driver.html', {"form" : form, "driver" : driver})
    else:
        form = PostRideAsDriverForm()
    return render(request, 'Rideshare_app/post_ride_driver.html', {"form" : form, "driver" : driver})

def post_ride_driver_result(request, driver_id):
    driver = get_object_or_404(Driver, pk = driver_id)
    #url = "/" + str(driver_id) + "/driver_profile"
    context = {"driver" : driver,  "driver_id" : driver_id}
    return render(request, 'Rideshare_app/post_ride_driver_result.html', context)


class RidesListView(generic.ListView):
    template_name = 'Rideshare_app/upcoming_rides_list.html'
    context_object_name = 'upcoming_rides_list'


    def get_queryset(self):
        # return all the upcoming trips
        return Ride.objects.filter(date__gte = timezone.now(), driver__isnull = False)
