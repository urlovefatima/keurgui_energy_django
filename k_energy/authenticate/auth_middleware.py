# myapp/auth_middleware.py
from django.shortcuts import redirect
from django.conf import settings
from django.urls import reverse

EXEMPT_URLS = [reverse('inscription'), reverse('inscription2'), reverse('connexion')]  # Ajouter les noms des vues publiques ici

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path

        if not request.user.is_authenticated and path not in EXEMPT_URLS:
            return redirect(settings.LOGIN_URL)

        return self.get_response(request)
