from django.contrib import admin
from django.urls import path
from app import views
<<<<<<< HEAD
from accueil.views import afficher_accueil, afficher_splashScreen, ajouter_piece, mdp_change
from appareil.views import appareilsView, piecesView, ajout_appareil, ajout_piece
from django.conf import settings
from django.conf.urls.static import static

=======
from accueil.views import afficher_accueil, afficher_splashScreen, ajouter_piece, mdp_change, afficher_historique
from appareil.views import appareilsView, piecesView, ajout_appareil, ajout_piece
from django.conf import settings
from django.conf.urls.static import static
from authenticate.views import register_step_one, register_step_two, connexion, logout_view
>>>>>>> e0df968938f99288701749fe5484c28d6eb3e3b8

urlpatterns = [
    path('admin/', admin.site.urls, name='page_admin'),
    path('', afficher_splashScreen),
    path('connexion/', connexion, name="connexion"),
    path('inscription/', register_step_one, name="inscription"),
    path('inscription2/',register_step_two, name="inscription2"),
    path('mdp/', views.afficher_page_mdp, name="mdp"),
    path('reset_password/', views.afficher_page_reset_mdp, name="reset_password"),
    path('ajouter_piece/', ajouter_piece),
    path('mdp_change/', mdp_change),
    path('accueil/', afficher_accueil, name="accueil"),
    path('pieces/', piecesView, name="pieces"),
    path('cons_piece/', views.afficher_cons_piece, name='cons'),
    path('appareils/', appareilsView, name='appareils'),
    path('historique/', afficher_historique, name = "historique"),
    path('notifications/', views.notifications_view, name='notifications'),
    path('ajout_appareil/', ajout_appareil, name='ajout_appareil'),
    path('ajout_piece/', ajout_piece, name='ajout_piece'),
<<<<<<< HEAD
=======
    path('logout/', logout_view, name='logout'),
>>>>>>> e0df968938f99288701749fe5484c28d6eb3e3b8
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

