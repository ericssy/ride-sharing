from django.contrib import admin
from .models import Ride, Rider, Driver, User
from django.contrib.admin.views.main import ChangeList


# Register your models here.

admin.site.register(Rider)
admin.site.register(Driver)
admin.site.register(Ride)
admin.site.register(User)
