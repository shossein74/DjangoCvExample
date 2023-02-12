from main.views import *
from django.urls import path

urlpatterns = [
    path('', home_view, name='home'),
]