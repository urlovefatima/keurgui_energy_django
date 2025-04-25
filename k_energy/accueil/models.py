from django.db import models

# Create your models here.


# models.py (ou juste une classe simple si tu ne l'enregistres pas dans la DB)
class PieceAccueil:
    def __init__(self, nom_piece, surface, imgUrl):
        self.nom_piece = nom_piece
        self.surface = surface
        self.imgUrl = imgUrl


class Appaccueil:
    def __init__ (self, nom_appareil, imgUrl, nom_piece):
        self.nom_appareil = nom_appareil
        self.imgUrl = imgUrl
        self.nom_piece = nom_piece
       
