from django.db import models
# from comptes.models import Eleve

# Create your models here.

# class de programme de formation ou de cours offert par l'ecole


class Programme(models.Model):
    nom = models.CharField(
        max_length=100,
        choices=(
            ('Marternel', 'Marternel'),
            ('Primaire', 'Primaire'),
            ('Secondaire', 'Secondaire'),
        ),
        default=None,
        null=True,
        help_text='Nom du programme',
        verbose_name='Nom du programme',

    )
    description = models.TextField(
        verbose_name='Description du programme',
        default=None,
        null=True,
        help_text='Description du programme',
    )
    duree = models.IntegerField(
        choices=(
            (1, '1 mois'),
            (2, '2 mois'),
            (3, '3 mois'),
            (4, '4 mois'),
            (5, '5 mois'),
            (6, '6 mois'),
            (7, '7 mois'),
            (8, '8 mois'),
            (9, '9 mois'),
            (10, '10 mois'),
            (11, '11 mois'),
            (12, '12 mois'),
        ),
        verbose_name='Durée du programme',
        default=None,
        null=True,
        help_text='Durée du programme',

    )
    montant = models.IntegerField(
        verbose_name='Montant du programme',
        default=None,
        null=True,
        help_text='Montant du programme',

    )

    def __str__(self):
        return self.nom

# class de classe


class Classe(models.Model):
    nom = models.CharField(
        max_length=100,
        choices=(
            ("Marternel",
             ("Clot d'enfant", "Clot d'enfant")
             ),
            ("Primaire",
                ("CP1", "CP1"),
                ("CP2", "CP2"),
                ("CE1", "CE1"),
                ("CE2", "CE2"),
                ("CM1", "CM1"),
                ("CM2", "CM2"),
             ),
            ("Secondaire",
                ("6ème", "6ème"),
                ("5ème", "5ème"),
                ("4ème", "4ème"),
                ("3ème", "3ème"),
             ),

        )),
    description = models.TextField()
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

# class de matricule


# class Matricule(models.Model):
#     eleve = models.ForeignKey('comptes.Eleve', on_delete=models.CASCADE)
#     classe = models.ForeignKey(Classe, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.matricule_id
