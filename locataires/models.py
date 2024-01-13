from django.db import models

# Create your models here.

class Locataire(models.Model):
    nom_complet = models.CharField(max_length=255)
    fonction = models.CharField(max_length=255)
    tel = models.IntegerField()
    adresse = models.TextField(max_length=255)
    def __str__(self) -> str:
        return f"{self.nom_complet}"