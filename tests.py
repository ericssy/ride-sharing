from django.test import TestCase
import unittest
from django.urls import resolve, reverse
from django.utils import timezone
from Rideshare_app.models import Ride, Rider, Driver
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
