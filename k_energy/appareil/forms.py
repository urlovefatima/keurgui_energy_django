from django import forms
from .models import Appareil, Piece

class AppareilForm(forms.ModelForm):
    class Meta:
        model = Appareil
        fields = ['nom', 'img', 'piece', 'actif']


class PieceForm(forms.ModelForm):
    class Meta:
        model = Piece
        fields = ['nom', 'img', 'surface']