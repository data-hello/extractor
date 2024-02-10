from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'myapp'  # This line is crucial

urlpatterns = [
    path('', BaseView, name='base'),
    path('leads/', LeadsView, name='leads'),
    path('customer/', CustomerView, name='customer'),
    # Add other URLs as needed
]