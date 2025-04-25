from django.db import models

# Create your models here.
class Appareil(models.Model):
    nom = models.CharField(max_length=256)
    piece = models.CharField(max_length=256)
    img = models.CharField(max_length=256)
    actif = models.BooleanField()

    def __str__(self):
        return f"{self.nom} {self.piece}"