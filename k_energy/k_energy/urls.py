
from django.contrib import admin
from django.urls import path ,include
from Api.views import RegisterStep1View, RegisterStep2View,LoginView,LogoutView
from rest_framework.authtoken.views import obtain_auth_token 
from accueil.views import afficher_accueil, afficher_splashScreen, ajouter_piece, mdp_change

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/step1/', RegisterStep1View.as_view(), name='register_step1'),
    path('api/register/step2/', RegisterStep2View.as_view(), name='register_step2'),
    path('api/auth/', include('rest_framework.urls')),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'), 
    path('api/auth/token/', obtain_auth_token, name='api_token_auth'),
    path('', afficher_splashScreen),
    path('ajouter_piece/', ajouter_piece),
    path('mdp_change/', mdp_change),
    path('accueil/', afficher_accueil)
]

