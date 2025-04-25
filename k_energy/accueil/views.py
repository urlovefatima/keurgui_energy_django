from django.shortcuts import render
from .models import PieceAccueil, Appaccueil

pieces = [
        PieceAccueil("Salon", "20m²", "img/salon.png"),
        PieceAccueil("Cuisine", "10m²", "img/cuisine.jpg"),
        PieceAccueil("Chambre parent", "16m²", "img/chambre_parent.jpg"),
        PieceAccueil("Chambre enfant1", "8m²", "img/chambre_enfant1.jpg"),
        PieceAccueil("Toilette publique", "12m²", "img/toilette.jpg"),
        PieceAccueil("Toilette parent", "12m²", "img/toilette.jpg"),
        PieceAccueil("Toilette enfant", "12m²", "img/toilette.jpg"),
    ]

appareils = [
        Appaccueil("Climatisateur(1)", "img/clim.jpg", "salon"),
        Appaccueil("Réfrigérateur", "img/frigo.jpg", "cuisine"),
        Appaccueil("Baffle", "img/baffle.webp", "Chambre enfant"),
        Appaccueil("micro-onde", "img/microwave.png", "cuisine"),
        Appaccueil("Télévision", "img/tele.png", "salon"),
        Appaccueil("Lampe", "img/lampe.webp", "Chambre parent"),
        Appaccueil("Humidifieur", "img/humidifier.webp", "cuisine"),
    ]

data = {"lespieces": pieces, "appauto": appareils}

def afficher_accueil(request):
    return render(request, "Accueil.html", context = data)



def afficher_splashScreen(request):
    return render(request, "splashScreen.html")

def ajouter_piece(request):
    return render(request, "ajouterPiece.html")

def mdp_change(request):
    return render(request, "mdpChange.html")