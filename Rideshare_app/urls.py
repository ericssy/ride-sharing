from django.contrib import admin
from django.urls import path

from . import views
from django.views.generic import TemplateView
from Rideshare_app import views
from .views import RidesListView

urlpatterns = [
 	path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('login', views.login, name='login'),
    path('<int:rider_id>/rider_profile', views.rider_profile, name= 'rider_profile'),
    path('<int:driver_id>/driver_profile', views.driver_profile, name= 'driver_profile'),
    path('<int:id>/ride', views.ride, name= 'ride'),
    path('rides', RidesListView.as_view(), name = "upcoming_rides_list"),
]
