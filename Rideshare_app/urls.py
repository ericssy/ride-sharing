from django.contrib import admin
from django.urls import path

from . import views
from django.views.generic import TemplateView
from Rideshare_app import views
from .views import RidesListView

urlpatterns = [
 	path('', views.index, name='index'),
    path('search', views.search, name='search'),
    #path('login', views.login, name='login'),
    path('<int:rider_id>/rider_profile', views.rider_profile, name= 'rider_profile'),
    path('<int:user_id>/profile', views.profile, name= 'profile'),
    path('<int:id>/ride', views.ride, name= 'ride'),
    path('rides', RidesListView.as_view(), name = "upcoming_rides_list"),
    path('<int:user_id>/profile/post_a_ride', views.post_ride_driver, name = "post_ride_driver"),
    path('<int:user_id>/profile/post_a_ride/success', views.post_ride_driver_result, name = "post_ride_driver_result"),
    path('<int:id>/ride/request_ride_result', views.request_ride_result, name = "request_ride_result"),
]
