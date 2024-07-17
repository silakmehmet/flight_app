from django.urls import path, include

from .views import RegisterCreateAPIView

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('register/', RegisterCreateAPIView.as_view()),

]
