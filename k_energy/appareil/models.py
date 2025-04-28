from django.db import models

# Create your models here.
class Piece(models.Model):
    nom = models.CharField(max_length=256)
    img = models.ImageField(upload_to='pieces/')
    surface = models.FloatField()

    def __str__(self):
        return f"{self.nom}"

class Appareil(models.Model):
    nom = models.CharField(max_length=256)
    piece = models.ForeignKey(Piece, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='appareils/')
    actif = models.BooleanField()

    def __str__(self):
        return f"{self.nom} {self.piece}"