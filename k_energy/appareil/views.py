from django.shortcuts import render
from .models import Appareil

# Create your views here.

def appareilsView(request):
    appareils = Appareil.objects.all()
    temp_name = 'appareils.html'
    context = {'appareils': appareils}
    return render(request, temp_name, context)