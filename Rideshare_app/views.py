from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Ride, Rider, Driver, User
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic.list import ListView
from .forms import PostRideAsDriverForm, RequestRideForm, SignUpForm
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return render(request, 'Rideshare_app/homepage.html')

def search(request):
    rides_list = Ride.objects.all()
    if request.GET.get('filter_departure_city'):
        rides_list = rides_list.filter(departure_location__iexact = request.GET.get('filter_departure_city'))
    if request.GET.get('filter_destination_city'):
        rides_list = rides_list.filter(destination_location__iexact = request.GET.get('filter_destination_city'))
    if request.GET.get('filter_date'):
        rides_list = rides_list.filter(date__gte = request.GET.get('filter_date'))
    else:
        rides_list = rides_list.filter(date__gte = timezone.now())
    filter_time = request.GET.get('filter_time')
    if filter_time == "Morning":
        rides_list = rides_list.filter(time__gte = "00:00:00", time__lte = "11:59:59")
    if filter_time == "Afternoon":
        rides_list = rides_list.filter(time__gte = "12:00:00", time__lte = "16:59:59")
    if filter_time == "Evening":
        rides_list = rides_list.filter(time__gte = "17:00:00", time__lte = "23:59:59")
    if request.GET.get('filter_price'):
        rides_list = rides_list.filter(price__lte = request.GET.get('filter_price'))
    if request.GET.get('filter_seats'):
        rides_list = rides_list.filter(seats__gte = request.GET.get('filter_seats'))

    avail_to_cities = Ride.objects.all().values('destination_location').distinct()
    avail_from_cities = Ride.objects.all().values('departure_location').distinct()
    avail_to_states = Ride.objects.all().values('destination_state').distinct()
    avail_from_states = Ride.objects.all().values('departure_state').distinct()

    context = {"rides_list" : rides_list, "avail_to_cities" : avail_to_cities, "avail_from_cities" : avail_from_cities, "avail_to_states" : avail_to_states, "avail_from_states" : avail_from_states}
    return render(request, 'Rideshare_app/search.html', context)

def login(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid() == True:
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            venmo = form.cleaned_data["venmo"]
            phone_number = form.cleaned_data["phone_number"]
            Rider.objects.create(first_name = first_name, last_name = last_name, email = email, venmo = venmo, phone_number = phone_number)
            Driver.objects.create(first_name = first_name, last_name = last_name, email = email, venmo = venmo, phone_number = phone_number)
            Current_Rider = Rider.objects.get(email=request.user.email)
            Current_Driver = Driver.objects.get(email=request.user.email)
            User.objects.create(first_name = first_name, last_name = last_name, email = email, venmo = venmo, phone_number = phone_number, driver = None, rider = None)
    else:
        form = SignUpForm()
    return render(request, 'Rideshare_app/sign_up_form.html', {"form" : form})

def getPendingRides(rider_id):
    all_rides = Rider.objects.all()
    ride_ids = []
    for ride in all_rides:
        if ride.pending_riders.filter(pk = rider_id).exists():
            ride_ids.append(ride.id)
    return ride_ids

def getPendingRides_driver(driver_id, rider_id):
    all_rides = Rider.objects.all()
    request_dict = {}
    for ride in all_rides:
        if ride.driver.driver_id == driver_id:
            if ride.pending_riders.filter(pk = rider_id).exists():
                request_dict[ride.id] = rider_id
    return request_dict


def rider_profile(request, rider_id):
    rider = get_object_or_404(Rider, pk = rider_id)


    ride = Ride.objects.filter(riders = rider_id, date__gte = timezone.now())
    # use for loops
    context = {"rider" : rider, "ride" : ride}
    return render(request, 'Rideshare_app/rider_profile.html', context)

def profile(request, user_id):
    user = get_object_or_404(User, pk = user_id)
    driver = user.driver
    rider = user.rider
    driver_id = driver.id
    rider_id = rider.id
    upcoming_rides_list = Ride.objects.filter(driver = driver_id, date__gte = timezone.now())
    past_rides = Ride.objects.filter(driver = driver_id, date__lt = timezone.now())

    pending_ride_ids = getPendingRides(rider_id)
    pending_rides_list = Ride.objects.filter(pk__in = pending_ride_ids, date__gte = timezone.now())



    context = {"user" : user, "driver" : driver, "upcoming_rides_list" : upcoming_rides_list,
                "past_rides" : past_rides, "rider" : rider,
                "pending_rides_list" : pending_rides_list}
    return render(request, 'Rideshare_app/profile.html', context)



def ride(request, id):
    ride = get_object_or_404(Ride, pk = id)
    if request.method == "POST":
        form = RequestRideForm(request.POST)
        if form.is_valid() == True:
            rider = Rider.objects.get(pk=7)
            ride.pending_riders.add(rider)
            # need to add if statements to determine if the car if full
            
            return HttpResponseRedirect(reverse('request_ride_result', args=(id,))) # here id refers to ride id
            #return render(request, 'Rideshare_app/post_ride_driver.html', {"form" : form, "driver" : driver})
    else:
        form = RequestRideForm()
    pending_riders = ride.pending_riders.all()
    confirmed_riders = ride.confirmed_riders.all()
    context = {"ride" : ride, "pending_riders" : pending_riders, "confirmed_riders" : confirmed_riders}
    return render(request, 'Rideshare_app/ride.html', context)

def post_ride_driver(request, user_id):
    user = get_object_or_404(User, pk = user_id)
    driver = user.driver
    driver_id = driver.id
    context = {"driver" : driver, "user_id" : user_id}
    if request.method == "POST":
        form = PostRideAsDriverForm(request.POST)
        if form.is_valid() == True:
            departure_location = form.cleaned_data["departure_location"]
            date = form.cleaned_data["date"]
            destination_location = form.cleaned_data["destination_location"]
            Ride.objects.create(date = date, driver = driver, departure_location = departure_location, destination_location = destination_location)
            return HttpResponseRedirect(reverse('post_ride_driver_result', args=(user_id,)))
            #return render(request, 'Rideshare_app/post_ride_driver.html', {"form" : form, "driver" : driver})
    else:
        form = PostRideAsDriverForm()
    return render(request, 'Rideshare_app/post_ride_driver.html', {"form" : form, "driver" : driver})

def post_ride_driver_result(request, user_id):
    user = get_object_or_404(User, pk = user_id)
    driver = user.driver
    driver_id = driver.id
    #url = "/" + str(driver_id) + "/driver_profile"
    context = {"driver" : driver,  "driver_id" : driver_id, "user" : user}
    return render(request, 'Rideshare_app/post_ride_driver_result.html', context)

def request_ride_result(request, id):
    ride = get_object_or_404(Ride, pk = id)
    context = {"ride" : ride}
    return render(request, 'Rideshare_app/request_ride_result.html', context)



class RidesListView(generic.ListView):
    template_name = 'Rideshare_app/upcoming_rides_list.html'
    context_object_name = 'upcoming_rides_list'
    def get_queryset(self):
        # return all the upcoming trips
        return Ride.objects.filter(date__gte = timezone.now(), driver__isnull = False)
