from django.urls import path
from .views import hello,home


urlpatterns = [
    path('hello', hello),
    path('', home),
]