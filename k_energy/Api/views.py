from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .serializers import RegisterStep1Serializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login ,logout
from rest_framework.authtoken.models import Token

class RegisterStep1View(APIView):
    def post(self, request):
        serializer = RegisterStep1Serializer(data=request.data)
        if serializer.is_valid():
            request.session['registration_data'] = serializer.validated_data
            return Response({'message': 'Etape 1 réussie. Passez à l\'étape 2.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class RegisterStep2View(APIView):
    def post(self, request):
        registration_data = request.session.get('registration_data')
        if not registration_data:
            return Response({'error': 'Aucune donnée d\'inscription trouvée en session.'}, status=status.HTTP_400_BAD_REQUEST)

        username = request.data.get('username')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')

        if password != confirm_password:
            return Response({'error': 'Les mots de passe ne correspondent pas.'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Ce nom d\'utilisateur est déjà pris.'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(
            first_name=registration_data['prenom'],
            last_name=registration_data['nom'],
            email=registration_data['email'],
            username=username,
            password=make_password(password),
        )

        request.session.pop('registration_data', None)

        return Response({'message': 'Utilisateur créé avec succès.'}, status=status.HTTP_201_CREATED)
    



class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Nom d\'utilisateur et mot de passe requis.'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            token, created = Token.objects.get_or_create(user=user)

            return Response({'message': 'Connexion réussie.', 'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Nom d\'utilisateur ou mot de passe incorrect.'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Déconnexion réussie.'}, status=status.HTTP_200_OK)        