from django.test import TestCase
import unittest
from django.urls import resolve, reverse
from django.utils import timezone
from Rideshare_app.models import Ride, Rider, Driver, User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect


class RideTestCase1(TestCase):
    def setUp(self):
        Driver.objects.create(first_name="Deepak", last_name="Goel", email="dzg4az@virginia.edu", venmo="DeepakG", phone_number="7034988423", car_make="Chrysler", car_model="200")
        driver1 = Driver.objects.get(email="dzg4az@virginia.edu")
        Ride.objects.create(departure_location="Ashburn, VA", destination_location="UVA", departure_state="Virginia", destination_state="Virginia", date=timezone.now(), time=timezone.now().time(), seats=4, price=15, driver=driver1)

    def test_user(self):
        ride1 = Ride.objects.get(departure_location="Ashburn, VA")
        ridePrice = ride1.price
        rideDriver = ride1.driver.first_name
        self.assertEqual(ridePrice, 15)
        self.assertEqual(rideDriver, "Deepak")


class RideTestCase2(TestCase):
    def setUp(self):
        Driver.objects.create(first_name="Shubhi", last_name= "Maheshwari", email="smv9t@virginia.edu", venmo="ShubhiM", phone_number="703456789", car_make="Honda", car_model="Accord")
        driver1 = Driver.objects.get(email="smv9t@virginia.edu")
        Ride.objects.create(departure_location="UVA", destination_location="New York City", departure_state="Virginia", destination_state="New york", date=timezone.now(), time=timezone.now().time(), seats=4, price=30, driver=driver1)

    def test_user(self):
        ride1 = Ride.objects.get(departure_location="UVA")
        rideSeats = ride1.seats
        rideDestination = ride1.destination_location
        self.assertEqual(rideSeats, 4)
        self.assertEqual(rideDestination, "New York City")


class RideTestCase3(TestCase):
    def setUp(self):
        Driver.objects.create(first_name="Trent", last_name="Ballard", email="tpb5fe@virginia.edu", venmo="TrentBallard", phone_number="7039634554", car_make="Ford", car_model="Windstar")
        driver1 = Driver.objects.get(email="tpb5fe@virginia.edu")
        Ride.objects.create(departure_location="Charlottesville", destination_location="Reston", departure_state="Virginia", destination_state="Virginia", date=timezone.now(), time=timezone.now().time(), seats=6, price=15, driver=driver1)

    def test_user(self):
        ride3 = Ride.objects.get(departure_location="Charlottesville")
        rideSeats = ride3.seats
        rideDestination = ride3.destination_location
        self.assertEqual(rideSeats, 6)
        self.assertEqual(rideDestination, "Reston")


class RideTestCase4(TestCase):
    def setUp(self):
        Driver.objects.create(first_name="Trent", last_name="Ballard", email="tpb5fe@virginia.edu", venmo="TrentBallard", phone_number="7039634554", car_make="Ford", car_model="Windstar")
        driver1 = Driver.objects.get(email="tpb5fe@virginia.edu")
        Ride.objects.create(departure_location="Charlottesville", destination_location="Reston", departure_state="Virginia", destination_state="Virginia", date=timezone.now(), time=timezone.now().time(), seats=6, price=15, driver=driver1)

    def test_user(self):
        ride3 = Ride.objects.get(departure_location="Charlottesville")
        ridePrice = ride3.price
        rideDestinationState = ride3.destination_state
        self.assertEqual(ridePrice, 15)
        self.assertEqual(rideDestinationState, "Virginia")


class RideTestCase5(TestCase):
    def setUp(self):
        Driver.objects.create(first_name="Trent", last_name="Ballard", email="tpb5fe@virginia.edu", venmo="TrentBallard", phone_number="7039634554", car_make="Ford", car_model="Windstar")
        driver1 = Driver.objects.get(email="tpb5fe@virginia.edu")
        Ride.objects.create(departure_location="Reston", destination_location="Charlottesville", departure_state="Virginia", destination_state="Virginia", date=timezone.now(), time=timezone.now().time(), seats=6, price=15, driver=driver1)

    def test_user(self):
        ride3 = Ride.objects.get(departure_location="Reston")
        rideDepartureState = ride3.departure_state
        self.assertEqual(rideDepartureState, "Virginia")


class RideTestCase6(TestCase):
    def setUp(self):
        Driver.objects.create(first_name="Trent", last_name="Ballard", email="tpb5fe@virginia.edu", venmo="TrentBallard", phone_number="7039634554", car_make="Ford", car_model="Windstar")
        driver1 = Driver.objects.get(email="tpb5fe@virginia.edu")
        Ride.objects.create(departure_location="Reston", destination_location="Charlottesville", departure_state="Virginia", destination_state="Virginia", date=timezone.now(), time=timezone.now().time(), seats=6, price=15, driver=driver1)

    def test_user(self):
        ride3 = Ride.objects.get(departure_location="Reston")
        rideDriver = ride3.driver
        rideDriver_fName = rideDriver.first_name
        rideDriver_lName = rideDriver.last_name
        self.assertEqual(rideDriver_fName, "Trent")
        self.assertEqual(rideDriver_lName, "Ballard")


class RideTestCase7(TestCase):
    def setUp(self):
        Driver.objects.create(first_name="Trent", last_name="Ballard", email="tpb5fe@virginia.edu", venmo="TrentBallard", phone_number="7039634554", car_make="Ford", car_model="Windstar")
        driver1 = Driver.objects.get(email="tpb5fe@virginia.edu")
        Ride.objects.create(departure_location="Reston", destination_location="Charlottesville", departure_state="Virginia", destination_state="Virginia", date=timezone.now(), time=timezone.now().time(), seats=6, price=15, driver=driver1)

    def test_user(self):
        ride3 = Ride.objects.get(departure_location="Reston")
        rideDriver = ride3.driver
        rideDriver_venmo = rideDriver.venmo
        self.assertEqual(rideDriver_venmo, "TrentBallard")


class RideTestCase8(TestCase):
    def setUp(self):
        Driver.objects.create(first_name="Trent", last_name="Ballard", email="tpb5fe@virginia.edu", venmo="TrentBallard", phone_number="7039634554", car_make="Ford", car_model="Windstar")
        driver1 = Driver.objects.get(email="tpb5fe@virginia.edu")
        Ride.objects.create(departure_location="Reston", destination_location="Charlottesville", departure_state="Virginia", destination_state="Virginia", date=timezone.now(), time=timezone.now().time(), seats=6, price=15, driver=driver1)

    def test_user(self):
        ride3 = Ride.objects.get(departure_location="Reston")
        rideDriver = ride3.driver
        rideDriver_make = rideDriver.car_make
        rideDriver_model = rideDriver.car_model
        self.assertEqual(rideDriver_make, "Ford")
        self.assertEqual(rideDriver_model, "Windstar")

class UserTestCase1(TestCase):
    def setUp(self):
        User.objects.create(first_name="Deepak", last_name="Goel", email="dzg4az@virginia.edu", venmo="DeepakG", phone_number="7034988423", driver=None, rider=None)

    def test_user(self):
        User1 = User.objects.get(first_name="Deepak")
        User1_email = User1.email
        self.assertEqual(User1_email, "dzg4az@virginia.edu")


class UserTestCase2(TestCase):
    def setUp(self):
        User.objects.create(first_name="Shubhi", last_name="Maheshwari", email="smv9t@virginia.edu", venmo="ShubhiM", phone_number="703456789", driver=None, rider=None)

    def test_user(self):
        User2 = User.objects.get(email="smv9t@virginia.edu")
        User2_venmo = User2.venmo
        self.assertEqual(User2_venmo, "ShubhiM")


class UserTestCase3(TestCase):
    def setUp(self):
        User.objects.create(first_name="Trent", last_name="Ballard", email="tpb5fe@virginia.edu", venmo="TrentBallard",
                            phone_number="7039634554", driver=None, rider=None)

    def test_user(self):
        User2 = User.objects.get(email="tpb5fe@virginia.edu")
        User2_phoneNum = User2.phone_number
        self.assertEqual(User2_phoneNum, "7039634554")


class UserTestCase4(TestCase):
    def setUp(self):
        User.objects.create(first_name="Trent", last_name="Ballard", email="tpb5fe@virginia.edu", venmo="TrentBallard",
                            phone_number="7039634554", driver=None, rider=None)

    def test_user(self):
        User3 = User.objects.get(email="tpb5fe@virginia.edu")
        User3_fName = User3.first_name
        User3_lName = User3.last_name
        self.assertEqual(User3_fName, "Trent")
        self.assertEqual(User3_lName, "Ballard")


class LoginTestCase(unittest.TestCase):
    def test_drivers_routes(self):
        resolver = resolve('/login/')
        self.assertEqual(resolver.view_name, 'django.views.generic.base.TemplateView')


class RidesListViewTests(TestCase):
    def test_empty_ride_list(self):
        response = self.client.get(reverse('upcoming_rides_list'))
        self.assertQuerysetEqual(response.context['upcoming_rides_list'], [])


class IndexTestCase(unittest.TestCase):
    def test_drivers_routes(self):
        resolver = resolve('/')
        self.assertNotEqual(resolver.view_name, 'django.views.generic.base.TemplateView')


class RiderTestCase1(TestCase):
    def setUp(self):
        Rider.objects.create(first_name="Deepak", last_name="Goel", email="dzg4az@virginia.edu", venmo="DeepakG", phone_number="7034988423")

    def test_user(self):
        Rider1 = Rider.objects.get(first_name="Deepak")
        Rider1_email = Rider1.email
        self.assertEqual(Rider1_email, "dzg4az@virginia.edu")


class RiderTestCase2(TestCase):
    def setUp(self):
        Rider.objects.create(first_name="Shubhi", last_name="Maheshwari", email="smv9t@virginia.edu", venmo="ShubhiM", phone_number="703456789")

    def test_user(self):
        Rider2 = Rider.objects.get(email="smv9t@virginia.edu")
        Rider2_venmo = Rider2.venmo
        self.assertEqual(Rider2_venmo, "ShubhiM")


class RiderTestCase3(TestCase):
    def setUp(self):
        Rider.objects.create(first_name="Trent", last_name="Ballard", email="tpb5fe@virginia.edu", venmo="TrentBallard", phone_number="7039634554")

    def test_user(self):
        Rider3 = Rider.objects.get(email="tpb5fe@virginia.edu")
        Rider3_venmo = Rider3.venmo
        self.assertEqual(Rider3_venmo, "TrentBallard")


class RiderTestCase4(TestCase):
    def setUp(self):
        Rider.objects.create(first_name="Trent", last_name="Ballard", email="tpb5fe@virginia.edu", venmo="TrentBallard", phone_number="7039634554")

    def test_user(self):
        rider3 = Rider.objects.get(email="tpb5fe@virginia.edu")
        rider3_phoneNum = rider3.phone_number
        self.assertEqual(rider3_phoneNum, "7039634554")


class RiderTestCase5(TestCase):
    def setUp(self):
        Rider.objects.create(first_name="Trent", last_name="Ballard", email="tpb5fe@virginia.edu", venmo="TrentBallard", phone_number="7039634554")

    def test_user(self):
        rider3 = Rider.objects.get(email="tpb5fe@virginia.edu")
        rider3_fName = rider3.first_name
        rider3_lName = rider3.last_name
        self.assertEqual(rider3_fName, "Trent")
        self.assertEqual(rider3_lName, "Ballard")
