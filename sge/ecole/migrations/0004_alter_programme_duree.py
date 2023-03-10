# Generated by Django 4.1.6 on 2023-02-08 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecole", "0003_remove_classe_nom"),
    ]

    operations = [
        migrations.AlterField(
            model_name="programme",
            name="duree",
            field=models.IntegerField(
                choices=[
                    (1, "1 mois"),
                    (2, "2 mois"),
                    (3, "3 mois"),
                    (4, "4 mois"),
                    (5, "5 mois"),
                    (6, "6 mois"),
                    (7, "7 mois"),
                    (8, "8 mois"),
                    (9, "9 mois"),
                    (10, "10 mois"),
                    (11, "11 mois"),
                ],
                default=None,
                help_text="Durée du programme",
                null=True,
                verbose_name="Durée du programme",
            ),
        ),
    ]
