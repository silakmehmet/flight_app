from django.db import models

from django.contrib.auth.models import User


class Flight(models.Model):
    flight_number = models.CharField(max_length=20)
    operation_airlines = models.CharField(max_length=50)
    departure_city = models.CharField(max_length=60)
    arrival_city = models.CharField(max_length=60)
    date_of_departure = models.DateField()
    estimated_time_of_departure = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"flight_number {self.flight_number} from {self.departure_city} to {self.arrival_city}"


class Passenger(models.Model):
    PASSENGER_TYPE = (
        (1, 'Adult'),
        (2, 'Child'),
        (3, 'Infant'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    create_date = models.DateTimeField(auto_now_add=True)
    passenger_type = models.PositiveSmallIntegerField(choices=PASSENGER_TYPE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    passenger = models.ManyToManyField(Passenger, related_name="passenger")
    flight = models.ForeignKey(
        Flight, on_delete=models.PROTECT, related_name="flight")

    def __str__(self):
        return f"Reservation by {self.user} for {self.passenger} on flight {self.flight}"
