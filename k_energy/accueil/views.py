from django.shortcuts import render

# Create your views here.

def afficher_accueil(request):
    return render(request, "Accueil.html")
