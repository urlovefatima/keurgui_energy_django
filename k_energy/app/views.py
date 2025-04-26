from django.shortcuts import render
from .models import Notification, Device

# Create your views here.

def afficher_page_connexion(request):
    return render(request, "connexion.html")

def afficher_page_inscription(request):
    return render(request,"inscription.html")

def afficher_page_mdp(request):
    return render(request, "mdp_oublie.html")

def afficher_page_reset_mdp(request):
    return render(request, "reset_password.html")

def afficher_pieces(request):
    return render(request, "pieces.html")

def afficher_cons_piece(request):
    return render(request,"pieces_cons.html")



# les views pour la partie notifications et historique 
def notifications_view(request):
    """Vue pour afficher la page des notifications"""
    notifications = Notification.objects.all()
    devices = Device.objects.all()
    
    context = {
        'notifications': notifications,
        'devices': devices,
    }
    
    return render(request, 'notifications.html', context)

def device_history_view(request):
    """Vue pour afficher la page d'historique complète des appareils"""
    devices = Device.objects.all().order_by('-active_since')
    
    context = {
        'devices': devices,
        'page_title': 'Historique des appareils'
    }
    
    return render(request, 'device_history.html', context)