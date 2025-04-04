from django.contrib import admin
from django.urls import path
from app import views
from accueil.views import afficher_accueil, afficher_splashScreen, ajouter_piece, mdp_change


urlpatterns = [
    path('admin/', admin.site.urls, name='page_admin'),
    path('', afficher_splashScreen),
    path('connexion/',views.afficher_page_connexion, name="connexion"),
    path('inscription/',views.afficher_page_inscription, name="inscription"),
    path('mdp/', views.afficher_page_mdp, name="mdp"),
    path('reset_password/', views.afficher_page_reset_mdp, name="reset_password"),
    path('ajouter_piece/', ajouter_piece),
    path('mdp_change/', mdp_change),
    path('accueil/', afficher_accueil, name="accueil"),
    path('pieces/', views.afficher_pieces, name="pieces"),
    path('cons_piece/', views.afficher_cons_piece, name='cons'),
]

