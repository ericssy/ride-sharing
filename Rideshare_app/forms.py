from django import forms
from django.forms import ModelForm
from Rideshare_app.models import Rider, Driver, Ride
from django.forms import HiddenInput

class PostRideAsDriverForm(ModelForm):

    class Meta:
        model = Ride
        fields = ("departure_location", "departure_state", "destination_location", "destination_state", "date", "time", "seats", "price")

class RequestRideForm(forms.Form):
    widgets = {'any_field': HiddenInput(),}
