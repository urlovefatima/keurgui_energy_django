from django.shortcuts import render

# Create your views here.

def afficher_page_connexion(request):
    return render(request, "connexion.html")

def afficher_page_inscription(request):
    return render(request,"inscription.html")

def afficher_page_mdp(request):
    return render(request, "mdp_oublie.html")

def afficher_page_reset_mdp(request):
    return render(request, "reset_password.html")