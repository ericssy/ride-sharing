from django.contrib import admin
from django.urls import path

from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name="Rideshare_app/login.html")),
    path('search', views.search, name='search'),
    path('login', views.login, name='login'),
    path('<int:rider_id>/rider_profile', views.rider_profile, name= 'rider_profile'),
    path('<int:driver_id>/driver_profile', views.driver_profile, name= 'driver_profile'),
    path('<int:id>/ride', views.ride, name= 'ride'),
]
