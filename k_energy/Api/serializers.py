from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterStep1Serializer(serializers.Serializer):
    nom = serializers.CharField(max_length=150)
    prenom = serializers.CharField(max_length=150)
    telephone = serializers.CharField(max_length=150)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Cet email est déjà utilisé.")
        return value


class RegisterStep2Serializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    confirmPassword = serializers.CharField(write_only=True)