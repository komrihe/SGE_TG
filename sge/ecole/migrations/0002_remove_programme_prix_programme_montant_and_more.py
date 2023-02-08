# Generated by Django 4.1.6 on 2023-02-08 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecole", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="programme", name="prix",),
        migrations.AddField(
            model_name="programme",
            name="montant",
            field=models.IntegerField(
                default=None,
                help_text="Montant du programme",
                null=True,
                verbose_name="Montant du programme",
            ),
        ),
        migrations.AlterField(
            model_name="programme",
            name="description",
            field=models.TextField(
                default=None,
                help_text="Description du programme",
                null=True,
                verbose_name="Description du programme",
            ),
        ),
        migrations.AlterField(
            model_name="programme",
            name="duree",
            field=models.IntegerField(
                default=None,
                help_text="Durée du programme",
                null=True,
                verbose_name="Durée du programme",
            ),
        ),
        migrations.AlterField(
            model_name="programme",
            name="nom",
            field=models.CharField(
                choices=[
                    ("Marternel", "Marternel"),
                    ("Primaire", "Primaire"),
                    ("Secondaire", "Secondaire"),
                ],
                default=None,
                help_text="Nom du programme",
                max_length=100,
                null=True,
                verbose_name="Nom du programme",
            ),
        ),
        migrations.DeleteModel(name="Matricule",),
    ]
