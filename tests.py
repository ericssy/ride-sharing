from django.test import TestCase
import unittest
from django.urls import resolve


class RoutesTestCase(unittest.TestCase):
    def test_drivers_routes(self):
        resolver = resolve('/login2/')
        self.assertEqual(resolver.view_name, 'django.views.generic.base.TemplateView')
    def test_drivers_routes(self):
        resolver = resolve('/accounts/')
        self.assertEqual(resolver.view_name, 'django.views.generic.base.TemplateView')
