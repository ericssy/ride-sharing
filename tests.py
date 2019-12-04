from django.test import TestCase
import unittest
from django.urls import resolve, reverse
from django.utils import timezone
from Rideshare_app.models import Ride, Rider, Driver, User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect

class RideTestCase1(TestCase):
    def setUp(self):
        Driver.objects.create(first_name="Deepak", last_name="Goel", email= "dzg4az@virginia.edu", venmo = "DeepakG", phone_number = "7034988423", car_make = "Chrysler", car_model = "200")
        Driver1 = Driver.objects.get(email = "dzg4az@virginia.edu")
        Ride.objects.create(departure_location = "Ashburn, VA", destination_location = "UVA", departure_state = "Virginia", destination_state = "Virginia", date = timezone.now(), time = timezone.now().time(), seats = 4, price = 15, driver = Driver1)

    def test_user(self):
        Ride1 = Ride.objects.get(departure_location = "Ashburn, VA")
        RidePrice = Ride1.price
        RideDriver = Ride1.driver.first_name
        self.assertEqual(RidePrice,15)
        self.assertEqual(RideDriver, "Deepak")

class RideTestCase2(TestCase):
    def setUp(self):
        Driver.objects.create(first_name="Shubhi", last_name= "Maheshwari", email = "smv9t@virginia.edu", venmo = "ShubhiM", phone_number = "703456789", car_make = "Honda", car_model = "Accord")
        Driver1 = Driver.objects.get(email = "smv9t@virginia.edu")
        Ride.objects.create(departure_location = "UVA", destination_location = "New York City", departure_state = "Virginia", destination_state = "New york", date = timezone.now(), time = timezone.now().time(), seats = 4, price = 30, driver = Driver1)

    def test_user(self):
        Ride1 = Ride.objects.get(departure_location = "UVA")
        RideSeats = Ride1.seats
        RideDestination = Ride1.destination_location
        self.assertEqual(RideSeats,4)
        self.assertEqual(RideDestination, "New York City")



class UserTestCase1(TestCase):
    def setUp(self):
        User.objects.create(first_name="Deepak", last_name="Goel", email= "dzg4az@virginia.edu", venmo = "DeepakG", phone_number = "7034988423", driver = None, rider = None)

    def test_user(self):
        User1 = User.objects.get(first_name="Deepak")
        User1_email = User1.email
        self.assertEqual(User1_email, "dzg4az@virginia.edu")

class UserTestCase2(TestCase):
    def setUp(self):
        User.objects.create(first_name="Shubhi", last_name= "Maheshwari", email = "smv9t@virginia.edu", venmo = "ShubhiM", phone_number = "703456789", driver = None, rider = None)
    def test_user(self):
        User2 = User.objects.get(email = "smv9t@virginia.edu")
        User2_venmo = User2.venmo
        self.assertEqual(User2_venmo, "ShubhiM")

class RidesListViewTests(TestCase):
    def test_empty_ride_list(self):
        response = self.client.get(reverse('upcoming_rides_list'))
        self.assertQuerysetEqual(response.context['upcoming_rides_list'],[])


class IndexTestCase(unittest.TestCase):
            def test_drivers_routes(self):
                resolver = resolve('/')
                self.assertNotEqual(resolver.view_name, 'django.views.generic.base.TemplateView')

class RiderTestCase1(TestCase):
    def setUp(self):
        Rider.objects.create(first_name="Deepak", last_name="Goel", email= "dzg4az@virginia.edu", venmo = "DeepakG", phone_number = "7034988423")

    def test_user(self):
        Rider1 = Rider.objects.get(first_name="Deepak")
        Rider1_email = Rider1.email
        self.assertEqual(Rider1_email, "dzg4az@virginia.edu")

class RiderTestCase2(TestCase):
    def setUp(self):
        Rider.objects.create(first_name="Shubhi", last_name= "Maheshwari", email = "smv9t@virginia.edu", venmo = "ShubhiM", phone_number = "703456789")

    def test_user(self):
        Rider2 = Rider.objects.get(email = "smv9t@virginia.edu")
        Rider2_venmo = Rider2.venmo
        self.assertEqual(Rider2_venmo, "ShubhiM")
