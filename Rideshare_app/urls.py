from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url

from . import views
from django.views.generic import TemplateView
from Rideshare_app import views
from .views import RidesListView
urlpatterns = [
 	path('', views.index, name='index'),
    path('search', views.search, name='search'),

    path('', include('social_django.urls', namespace='social')),
    url(r'^account/', include('social_django.urls', namespace='social')),
    #url(r'^account/', include('django.contrib.auth.urls', namespace='auth')),
    path('accounts/', include('django.contrib.auth.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    path('login2', views.login, name='login'),
    path('sign_up', views.sign_up, name = 'sign_up'),
    path('auth/', include(('social_django.urls', 'social_django'), namespace='social')),
    path('logout', views.Logout, name = 'logout'),
    path('google_sign_up', views.google_sign_up, name = "google_sign_up"),
    path('<int:rider_id>/rider_profile', views.rider_profile, name= 'rider_profile'),
    path('<int:user_id>/profile', views.profile, name= 'profile'),
    path('<int:id>/ride', views.ride, name= 'ride'),
    path('rides', RidesListView.as_view(), name = "upcoming_rides_list"),
    path('<int:user_id>/profile/post_a_ride', views.post_ride_driver, name = "post_ride_driver"),
    path('<int:user_id>/profile/post_a_ride/success', views.post_ride_driver_result, name = "post_ride_driver_result"),
    path('<int:id>/ride/request_ride_result', views.request_ride_result, name = "request_ride_result"),
    #path('google_login_result', views.google_login_result, name = "google_login_result"),
]
