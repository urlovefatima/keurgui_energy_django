from django.contrib import admin
from django.urls import path
from app import views
from accueil.views import afficher_accueil, afficher_splashScreen, ajouter_piece, mdp_change
from appareil.views import appareilsView, piecesView, ajout_appareil, ajout_piece
from django.conf import settings
from django.conf.urls.static import static


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
    path('pieces/', piecesView, name="pieces"),
    path('cons_piece/', views.afficher_cons_piece, name='cons'),
    path('appareils/', appareilsView, name='appareils'),
    path('notifications/', views.notifications_view, name='notifications'),
    path('ajout_appareil/', ajout_appareil, name='ajout_appareil'),
    path('ajout_piece/', ajout_piece, name='ajout_piece'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

