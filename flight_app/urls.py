from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import FlightMVS, ReservationMVS, PassengerMVS


router = DefaultRouter()
router.register("flights", FlightMVS)
router.register("reservations", ReservationMVS)
router.register("passengers", PassengerMVS)

urlpatterns = [
    path("", include(router.urls))

]
