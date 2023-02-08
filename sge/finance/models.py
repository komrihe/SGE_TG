from django.db import models

# Create your models here.
#   financement de la formation de l'élève


class Financement(models.Model):
    nom = models.CharField(
        max_length=50,
        choices=(
            ('Bourse', 'Bourse'),
            ('Paiement direct', 'Paiement direct'),
            ('Paiement en plusieurs fois', 'Paiement en plusieurs fois'),

        ),
        unique=True)
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.nom

# Account payable de l'élève


class CompteAPayer(models.Model):
    eleve = models.ForeignKey('comptes.Eleve', on_delete=models.CASCADE)
    programme = models.ForeignKey(
        'ecole.Programme', on_delete=models.CASCADE)
    # classe = models.ForeignKey('ecole.Classe', on_delete=models.CASCADE)
    financement = models.ForeignKey(Financement, on_delete=models.CASCADE)
    status_de_paiement = models.BooleanField(default=False)
    montant_a_payer = models.DecimalField(max_digits=10, decimal_places=2)
    date_de_paiement = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True
    )
    paiement_en_raison_de = models.CharField(
        max_length=50, blank=True, null=True)
    note = models.TextField(max_length=500, blank=True, null=True)

    def calculer_montant(self):
        self.montant = self.programme.montant
        if self.financement.nom == 'Bourse':
            self.montant = self.montant - (self.montant * 0.2)
        elif self.financement.nom == 'Paiement direct':
            self.montant = self.montant
        elif self.financement.nom == 'Paiement en plusieurs fois':
            self.montant = self.montant + (self.montant * 0.2)
        if self.paiement_en_raison_de:
            self.montant = self.montant + (self.montant * 0.2)

        return self.montant

        pass

    def __str__(self):
        return self.eleve
