from django.db import models

# Create your models here.
class Batiment(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    nombre_appartement = models.IntegerField()
    def __str__(self) -> str:
        return f"{self.nom}"



class Appartement(models.Model):
    batiment = models.ForeignKey(Batiment, on_delete=models.CASCADE)
    numero = models.IntegerField()
    surface = models.DecimalField(max_digits=10, decimal_places=2)
    prix = models.DecimalField(max_digits=10, decimal_places=2)