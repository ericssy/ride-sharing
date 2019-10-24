from django.db import models

# Create your models here.

class Rider(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 100)

    def __str__(self):
        return self.first_name + " " + self.last_name;


class Driver(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 100)

    def __str__(self):
        return self.first_name + " " + self.last_name;


class Ride(models.Model):
    departure_location = models.CharField(max_length = 30)
    destination_location = models.CharField(max_length = 30)
    date = models.DateField()
    # each ride links to only one driver
    driver = models.ForeignKey(Driver, null = True, on_delete = models.CASCADE)
    riders = models.ManyToManyField(Rider)

    def __str__(self):
        return self.driver.first_name + "'s ride from " + self.departure_location + " to "
        + self.destination_location + " on " + self.date;
