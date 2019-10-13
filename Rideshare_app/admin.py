from django.contrib import admin
from .models import Ride, Rider, Driver


# Register your models here.
admin.site.register(Ride)
admin.site.register(Rider)
admin.site.register(Driver)
