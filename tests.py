from django.test import TestCase
import unittest
from django.urls import resolve


class RoutesTestCase(unittest.TestCase):
    def test_drivers_routes(self):
        resolver = resolve('/drivers/')
        self.assertEqual(resolver.view_name, 'drivers_landing')
