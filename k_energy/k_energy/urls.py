"""
URL configuration for k_energy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from Api.views import RegisterStep1View, RegisterStep2View,LoginView,LogoutView
from rest_framework.authtoken.views import obtain_auth_token 
from accueil import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/step1/', RegisterStep1View.as_view(), name='register_step1'),
    path('api/register/step2/', RegisterStep2View.as_view(), name='register_step2'),
    path('api/auth/', include('rest_framework.urls')),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'), 
    path('api/auth/token/', obtain_auth_token, name='api_token_auth'),
    path('', views.afficher_accueil)
]
