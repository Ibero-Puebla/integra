from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'users/index.html')

def users(request, question_id):
    return HttpResponse("Lista de usuarios %s." % question_id)

def devices(request, question_id):
    response = "Lista de dispostivos %s."
    return HttpResponse(response % question_id)

def humidity(request, question_id):
    return HttpResponse("Humedad %s." % question_id)

def temperature(request, question_id):
    return HttpResponse("Temperatura %s." % question_id)

def uvauvb(request, question_id):
    return HttpResponse("UVA - UVB %s." % question_id)

def air(request, question_id):
    return HttpResponse("Calidad del aire %s." % question_id)
