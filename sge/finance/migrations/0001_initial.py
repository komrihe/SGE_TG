# Generated by Django 4.1.6 on 2023-02-08 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("comptes", "0006_alter_eleve_autre_prenom"),
        ("ecole", "0002_remove_programme_prix_programme_montant_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Financement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nom",
                    models.CharField(
                        choices=[
                            ("Bourse", "Bourse"),
                            ("Paiement direct", "Paiement direct"),
                            (
                                "Paiement en plusieurs fois",
                                "Paiement en plusieurs fois",
                            ),
                        ],
                        max_length=50,
                        unique=True,
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CompteAPayer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status_de_paiement", models.BooleanField(default=False)),
                (
                    "montant_a_payer",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("date_de_paiement", models.DateField(blank=True, null=True)),
                (
                    "paiement_en_raison_de",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("note", models.TextField(blank=True, max_length=500, null=True)),
                (
                    "eleve",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="comptes.eleve"
                    ),
                ),
                (
                    "financement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="finance.financement",
                    ),
                ),
                (
                    "programme",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ecole.programme",
                    ),
                ),
            ],
        ),
    ]
