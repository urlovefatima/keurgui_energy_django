from django.shortcuts import render

# Create your views here.

def afficher_accueil(request):
    return render(request, "Accueil.html")


def afficher_splashScreen(request):
    return render(request, "splashScreen.html")

def ajouter_piece(request):
    return render(request, "ajouterPiece.html")

def mdp_change(request):
    return render(request, "mdpChange.html")