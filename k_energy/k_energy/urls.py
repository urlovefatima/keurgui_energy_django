from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('admin/', admin.site.urls, name='page_admin'),
    path('connexion/',views.afficher_page_connexion, name="connexion"),
    path('inscription/',views.afficher_page_inscription, name="inscription"),
    path('mdp/', views.afficher_page_mdp, name="mdp"),
    path('reset_password/', views.afficher_page_reset_mdp, name="reset_password"),
]
