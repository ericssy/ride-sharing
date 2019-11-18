from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Ride, Rider, Driver, User
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic.list import ListView
from .forms import PostRideAsDriverForm, RequestRideForm, SignUpForm
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date

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
            try:
                Current_User = User.objects.get(email=email)
            except:
                Rider.objects.create(first_name = first_name, last_name = last_name, email = email, venmo = venmo, phone_number = phone_number)
                Driver.objects.create(first_name = first_name, last_name = last_name, email = email, venmo = venmo, phone_number = phone_number)
                Current_Rider = Rider.objects.get(email=email)
                Current_Driver = Driver.objects.get(email=email)
                User.objects.create(first_name = first_name, last_name = last_name, email = email, venmo = venmo, phone_number = phone_number, driver = Current_Driver, rider = Current_Rider)
            else:
                return render(request, 'Rideshare_app/sign_up_form.html', {"form" : form, "user_flag" : True})


    else:
        form = SignUpForm()
    return render(request, 'Rideshare_app/sign_up_form.html', {"form" : form, "user_flag" : False})

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
    upcoming_drives = Ride.objects.filter(driver = driver_id, date__gte = timezone.now())
    past_drives = Ride.objects.filter(driver = driver_id, date__lt = timezone.now())
    upcoming_rides = []
    past_rides = []
    for i in Ride.objects.all():
        if rider in i.confirmed_riders.all():
            if i.date >= date.today():
                upcoming_rides.append(i)
            else:
                past_rides.append(i)

    context = {"user" : user, "driver" : driver, "rider" : rider, "upcoming_drives" : upcoming_drives, "past_drives" : past_drives, "upcoming_rides" : upcoming_rides, "past_rides" : past_rides}
    return render(request, 'Rideshare_app/profile.html', context)



def ride(request, id):
    ride = get_object_or_404(Ride, pk = id)
    rider = Rider.objects.get(pk=4)
    if request.method == "POST":
        form = RequestRideForm(request.POST)
        if form.is_valid() == True:
            if rider in ride.confirmed_riders.all():
                ride.confirmed_riders.remove(rider)
                ride.seats = ride.seats + 1
                ride.save()
            elif rider not in ride.confirmed_riders.all() and ride.seats > 0:
                ride.confirmed_riders.add(rider)
                ride.seats = ride.seats - 1
                ride.save()
            # need to add if statements to determine if the car if full

            return HttpResponseRedirect(reverse('request_ride_result', args=(id,))) # here id refers to ride id
            #return render(request, 'Rideshare_app/post_ride_driver.html', {"form" : form, "driver" : driver})
    else:
        form = RequestRideForm()
    pending_riders = ride.pending_riders.all()
    confirmed_riders = ride.confirmed_riders.all()
    context = {"ride" : ride, "pending_riders" : pending_riders, "confirmed_riders" : confirmed_riders, "user" : rider}
    return render(request, 'Rideshare_app/ride.html', context)

def post_ride_driver(request, user_id):
    user = get_object_or_404(User, pk = user_id)
    driver = user.driver
    driver_id = driver.id
    context = {"driver" : driver, "user_id" : user_id}
    ride = ""
    if request.method == "POST":
        form = PostRideAsDriverForm(request.POST)
        if form.is_valid() == True:
            departure_location = form.cleaned_data["departure_location"]
            departure_state = form.cleaned_data["departure_state"]
            destination_location = form.cleaned_data["destination_location"]
            destination_state = form.cleaned_data["destination_state"]
            date = form.cleaned_data["date"]
            time = form.cleaned_data["time"]
            price = form.cleaned_data["price"]
            seats = form.cleaned_data["seats"]

            ride = Ride(date = date, driver = driver, departure_location = departure_location, destination_location = destination_location, departure_state = departure_state, destination_state = destination_state, price = price, seats = seats, time = time)
            ride.save()
            # ride = Ride.objects.create(date = date, driver = driver, departure_location = departure_location, destination_location = destination_location, departure_state = departure_state, destination_state = destination_state, price = price, seats = seats)
            return HttpResponseRedirect(reverse('post_ride_driver_result', args=(user_id,)))
            #return render(request, 'Rideshare_app/post_ride_driver.html', {"form" : form, "driver" : driver})
    else:
        form = PostRideAsDriverForm()
    return render(request, 'Rideshare_app/post_ride_driver.html', {"form" : form, "driver" : driver, "ride" : ride})

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
