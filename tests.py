from django.test import TestCase
import unittest
from django.urls import resolve, reverse
from django.utils import timezone
from Rideshare_app.models import Ride, Rider, Driver, User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect

class RoutesTestCase(unittest.TestCase):
    def test_drivers_routes(self):
        resolver = resolve('/login/')
        self.assertEqual(resolver.view_name, 'django.views.generic.base.TemplateView')


class RidesListViewTests(TestCase):
    def test_empty_ride_list(self):
        response = self.client.get(reverse('upcoming_rides_list'))
        self.assertQuerysetEqual(response.context['upcoming_rides_list'],[])

class UserTestCases(TestCase):
    def setUp(self):
        User.objects.create(first_name="Deepak", last_name="Goel", email= "dzg4az@virginia.edu", venmo = "DeepakG", phone_number = "7034988423", driver = None, rider = None)
        User.objects.create(first_name="Shubhi", last_name= "Maheshwari", email = "smv9t@virginia.edu", venmo = "ShubhiM", phone_number = "703456789", driver = None, rider = None)

    def test_user(self):
        User1 = User.objects.get(first_name="Deepak")
        User1_email = User1.email
        self.assertEqual(User1_email, "dzg4az@virginia.edu")
        User2 = User.objects.get(email = "smv9t@virginia.edu")
        User2_venmo = User2.venmo
        self.assertEqual(User2_venmo, "ShubhiM")
