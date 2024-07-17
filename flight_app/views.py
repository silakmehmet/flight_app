from rest_framework.viewsets import ModelViewSet

from .serializers import FlightSerializer, ReservationSerializer, PassengerSerializer
from .models import Flight, Reservation, Passenger
from .permissions import IsAdminOrReadOnly


class FlightMVS(ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAdminOrReadOnly]


class ReservationMVS(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class PassengerMVS(ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
