from django.db import models
from locataires.models import Locataire
# Create your models here.


class VersementManager(models.Manager):
    def versement_exists_for_month(self, locataire, date_paiement):
        return self.filter(locataire=locataire, date_paiement__month=date_paiement.month).exists()

class Versement(models.Model):
    locataire = models.ForeignKey(Locataire, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_paiement = models.DateField()
    status_validation = models.BooleanField(default=False)

    class Meta:
        unique_together = ['locataire','date_paiement']

    def __str__(self):
        return f"Versement de {self.locataire} de {self.montant} le {self.date_paiement}"