from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse

@login_required
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

def handler404(request):
    return render(request, 'users/404.html', status=404)

def handler500(request):
    return render(request, 'users/500.html', status=500)
