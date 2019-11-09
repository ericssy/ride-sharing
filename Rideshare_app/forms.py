from django import forms
from django.forms import ModelForm
from Rideshare_app.models import Rider, Driver, Ride
from django.forms import HiddenInput

class PostRideAsDriverForm(ModelForm):

    class Meta:
        model = Ride
        fields = ('date', "departure_location", "destination_location")

class RequestRideForm(forms.Form):
    widgets = {'any_field': HiddenInput(),}
