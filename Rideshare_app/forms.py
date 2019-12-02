from django import forms
from django.forms import ModelForm
from Rideshare_app.models import Rider, Driver, Ride, User
from django.contrib.auth.models import User as User_Auth
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
    seats = forms.IntegerField(label='Seats Available', initial=1, min_value=1, validators=[MinValueValidator(1)])
    price = forms.IntegerField(label='Price', initial=0, min_value=0, validators=[MinValueValidator(0)])

class RequestRideForm(forms.Form):
    widgets = {'any_field': HiddenInput(),}

class SignUpForm(forms.Form):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email Address')
    venmo = forms.CharField(label='Venmo Account')
    phone_number = forms.CharField(label='Phone Number', max_length=10, min_length=10)

class LoginForm(forms.Form):
    email = forms.CharField(label='email')
    
