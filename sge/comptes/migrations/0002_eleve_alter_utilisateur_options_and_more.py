# Generated by Django 4.1.6 on 2023-02-08 01:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("comptes", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Eleve",
            fields=[
                (
                    "utilisateur",
                    models.OneToOneField(
                        help_text="Compte de l'élève",
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Compte de l'élève",
                    ),
                ),
                (
                    "nom",
                    models.CharField(
                        default=None,
                        help_text="Nom de l'élève",
                        max_length=50,
                        null=True,
                        verbose_name="Nom de l'élève",
                    ),
                ),
                (
                    "prenom",
                    models.CharField(
                        default=None,
                        help_text="Prénom de l'élève",
                        max_length=50,
                        null=True,
                        verbose_name="Prénom de l'élève",
                    ),
                ),
                ("autre_prenom", models.CharField(max_length=50)),
                (
                    "date_de_naissance",
                    models.DateField(
                        default=None,
                        help_text="Date de naissance",
                        null=True,
                        verbose_name="Date de naissance",
                    ),
                ),
                (
                    "telephone",
                    models.CharField(
                        default=None,
                        help_text="Téléphone",
                        max_length=50,
                        null=True,
                        verbose_name="Téléphone",
                    ),
                ),
                (
                    "adresse",
                    models.CharField(
                        default=None,
                        help_text="Adresse",
                        max_length=50,
                        null=True,
                        verbose_name="Adresse",
                    ),
                ),
                (
                    "prefecture",
                    models.CharField(
                        default=None,
                        help_text="Préfecture",
                        max_length=50,
                        null=True,
                        verbose_name="Préfecture",
                    ),
                ),
                (
                    "ville",
                    models.CharField(
                        default=None,
                        help_text="Ville",
                        max_length=50,
                        null=True,
                        verbose_name="Ville",
                    ),
                ),
                (
                    "quartier",
                    models.CharField(
                        default=None,
                        help_text="Quartier",
                        max_length=50,
                        null=True,
                        verbose_name="Quartier",
                    ),
                ),
                (
                    "code_postal",
                    models.CharField(
                        default=None,
                        max_length=50,
                        null=True,
                        verbose_name="Code postal",
                    ),
                ),
                (
                    "pays",
                    models.CharField(
                        default=None,
                        help_text="Pays",
                        max_length=50,
                        null=True,
                        verbose_name="Pays",
                    ),
                ),
            ],
        ),
        migrations.AlterModelOptions(name="utilisateur", options={},),
        migrations.RemoveField(model_name="utilisateur", name="date_joined",),
        migrations.RemoveField(model_name="utilisateur", name="first_name",),
        migrations.RemoveField(model_name="utilisateur", name="groups",),
        migrations.RemoveField(model_name="utilisateur", name="is_admin",),
        migrations.RemoveField(model_name="utilisateur", name="is_superuser",),
        migrations.RemoveField(model_name="utilisateur", name="last_name",),
        migrations.RemoveField(model_name="utilisateur", name="user_permissions",),
    ]