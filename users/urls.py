from django.urls import path
from rest_framework import urlpatterns
from users.views import RegisterView

urlpatterns = [
    path('auth/register', RegisterView.as_view())
]