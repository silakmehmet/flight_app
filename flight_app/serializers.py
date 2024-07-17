from rest_framework import serializers

from .models import Flight, Passenger, Reservation


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = "__all__"
        read_only_fields = ["id"]


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = "__all__"
        read_only_fields = ["id", "created_date"]


class ReservationSerializer(serializers.ModelSerializer):
    passenger = PassengerSerializer(many=True)
    flight_number = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = "__all__"
        read_only_fields = ["id", "flight_number"]

    def get_flight_number(self, obj):
        return obj.flight.flight_number
