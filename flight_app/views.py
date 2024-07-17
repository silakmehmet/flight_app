from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

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
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset

        return queryset.filter(user=self.request.user)


class PassengerMVS(ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
