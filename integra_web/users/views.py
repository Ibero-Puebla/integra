from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'users/index.html')

def users(request):
    return render(request, 'users/users.html')

def devices(request):
    return render(request, 'users/devices.html')

def humidity(request):
    return render(request, 'users/humidity.html')

def temperature(request):
    return render(request, 'users/temperature.html')

def uvauvb(request):
    return render(request, 'users/uvauvb.html')

def air(request):
    return render(request, 'users/air.html')

def industry(request):
    return render(request, 'users/industry.html')

def voltage(request):
    return render(request, 'users/voltage.html')

def pressure(request):
    return render(request, 'users/pressure.html')

def vibration(request):
    return render(request, 'users/vibration.html')
