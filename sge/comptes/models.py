import datetime, time
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone, dateformat, formats

#rgxvalidator
from django.core.validators import RegexValidator


#import AbstractUser
from django.contrib.auth.models import AbstractUser

# Create your models here.
# AbstractUserManager is a class that contains all the fields of the user


class GestionDutilisateurs(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Les utilisateurs doivent avoir une adresse mail')

        utilisateur = self.model(
            email=self.normalize_email(email),
        )

        utilisateur.set_password(password)
        utilisateur.save(using=self._db)
        return utilisateur

    def create_superuser(self, email, password, **extra_fields):
        extra_fields = {'is_staff': True}
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        utilisateur = self.create_user(
            email,
            password=password,
            **extra_fields
        )
        utilisateur.is_superuser = True
        utilisateur.save(using=self._db)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

    def create_staffuser(self, email, password):
        extra_fields = {'is_staff': True}
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        utilisateur = self.create_user(
            email,
            password=password,
            **extra_fields
        )
        utilisateur.is_admin = True
        utilisateur.save(using=self._db)

        if utilisateur.is_superuser:
            raise ValueError('Staffuser must have is_superuser=False.')

        if not utilisateur.is_personnel:
            raise ValueError('Staffuser must have est_personnel=True.')
        return utilisateur


class Utilisateur(AbstractBaseUser):
    username = None
    email = models.EmailField(
        verbose_name='adresse mail',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    date_d_inscription = models.DateTimeField(auto_now_add=True)

    objects = GestionDutilisateurs()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the utilisateur have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the utilisateur have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_admin(self):
        "Is the utilisateur a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    # @property
    def is_staff(self):
        "Is the utilisateur a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_staff

    def get_nom_court(self):
        return self.email

    def get_nom_complet(self):
        return self.email

    def get_identifiant(self):
        return self.email

    def get_email(self):
        return self.email

    pass


# class d'eleve qui herite de la classe utilisateur

class Eleve(models.Model):
    #unique matricule pour chaque eleve
    #generate matricule
    matricule_id = models.CharField(
        primary_key=True,
        null=False,
        # default=None,
        max_length=10,
        validators=[
            RegexValidator(
                regex="^[0-9]{10}$",
                message="Le matricule doit etre compose de 10 chiffres",
                code="invalid_matricule",
            )
        ],
        unique=True,
        help_text="Le matricule doit etre compose de 10 chiffres",
        error_messages={},
        verbose_name="Le numero de Matricule",
    )

    def save(self, *args, **kwargs):
        if not self.matricule_id:
            self.matricule_id = self.generate_matricule_id()
            super().save(*args, **kwargs)

    def generate_matricule_id(self):
        #get current year
        def get_current_year():
            now = timezone.now()
            return now.year
        annee_actuelle = get_current_year()
        return f"{annee_actuelle}{self.prenom[0].capitalize()}{self.nom.capitalize()[0]}{str(int(time.time()))}"

    utilisateur = models.OneToOneField(
        to=Utilisateur,
        on_delete=models.CASCADE,
        # primary_key=True,
        help_text='Compte de l\'élève',
        verbose_name='Compte de l\'élève',
        # null=True,

    )
    nom = models.CharField(
        max_length=50,
        verbose_name='Nom de l\'élève',
        default=None,
        null=True,
        help_text='Nom de l\'élève',
        # null=True,
    )
    prenom = models.CharField(
        max_length=50,
        verbose_name='Prénom de l\'élève',
        default=None,
        null=True,
        help_text='Prénom de l\'élève',
    )
    autre_prenom = models.CharField(
        max_length=50,
        verbose_name='Autre prénom de l\'élève',
        default=None,
        null=False,
        blank=True,
        help_text='Autre prénom de l\'élève',
    )
    date_de_naissance = models.DateField(
        verbose_name='Date de naissance',
        default=None,
        null=True,
        help_text='Date de naissance',

    )
    telephone = models.CharField(
        max_length=50,
        verbose_name='Téléphone de l\'élève',
        default=None,
        null=True,
        help_text='Téléphone de l\'élève',
    )
    adresse = models.CharField(
        max_length=50,
        verbose_name='Adresse de l\'élève',
        default=None,
        null=True,
        help_text='Adresse de l\'élève',
    )

    prefecture = models.CharField(
        max_length=50,
        verbose_name='Préfecture',
        default=None,
        null=True,
        help_text='Préfecture',

    )

    ville = models.CharField(
        max_length=50,
        verbose_name='Ville',
        default=None,
        null=True,
        help_text='Ville',
    )
    quartier = models.CharField(
        max_length=50,
        verbose_name='Quartier',
        default=None,
        null=True,
        help_text='Quartier',
    )
    code_postal = models.CharField(
        max_length=50,
        verbose_name='Code postal',
        default=None,
        null=True,
        help_text='Code postal',

    )
    pays = models.CharField(
        max_length=50,
        verbose_name='Pays',
        default=None,
        null=True,
        help_text='Pays',
    )
    #classe = models.ForeignKey(Classe, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
    
    def __str__(self):
        return self.matricule_id

    def get_nom_complet(self):
        if self.autre_prenom:
            return self.nom + ' ' + self.prenom + ' ' + self.autre_prenom
        else:
            return self.nom + ' ' + self.prenom

    def  nom_complet(self):
        return self.get_nom_complet().upper()
    def get_nom_court(self):
        return self.nom

    def get_identifiant(self):
        return self.nom

    def get_email(self):
        return self.email

    pass
