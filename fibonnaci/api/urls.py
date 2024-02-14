from django.urls import path

from api.views import FibonacciAPI

urlpatterns = [
    path('api/<int:pk>', FibonacciAPI.as_view()),
]