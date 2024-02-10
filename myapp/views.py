from django.shortcuts import render
from .models import *
# Create your views here.

def BaseView(request):
    return render(request, 'myapp/dashboard.html')


def LeadsView(request):
    return render(request, 'myapp/leads.html')

def CustomerView(request):
    return render(request,'myapp/customer.html')

