from django import forms
from django.forms import ModelForm
from Rideshare_app.models import Rider, Driver, Ride, User
from django.forms import HiddenInput
from django.core.validators import MinValueValidator

class PostRideAsDriverForm(forms.Form):
    forms.DateInput.input_type="date"
    forms.TimeInput.input_type="time"

    departure_location = forms.CharField(label='Departure City')
    departure_state = forms.CharField(label='Departure State')
    destination_location = forms.CharField(label='Destination City')
    destination_state = forms.CharField(label='Destination State')
    date = forms.DateField(label='Departure Date')
    time = forms.TimeField(label='Departure Time')
    seats = forms.IntegerField(label='Seats Available', initial=1, validators=[MinValueValidator(1)])
    price = forms.IntegerField(label='Price', initial=0, validators=[MinValueValidator(0)])

class RequestRideForm(forms.Form):
    widgets = {'any_field': HiddenInput(),}

class SignUpForm(ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'venmo', 'phone_number')
