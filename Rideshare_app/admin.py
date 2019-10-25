from django.contrib import admin
from .models import Ride, Rider, Driver
from django.contrib.admin.views.main import ChangeList


# Register your models here.

admin.site.register(Rider)
admin.site.register(Driver)
admin.site.register(Ride)
