from django.contrib import admin

from .models import *


# Register your models here.
@admin.register(Utilisateur)
class UtilisateursAdmin(admin.ModelAdmin):
    list_display = ('email', )
    # list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


@admin.register(Eleve)
class ElevesAdmin(admin.ModelAdmin):
    exclude = ('matricule_id',)
    list_display = ('nom_complet',
                    'matricule_id',
                    'date_de_naissance',
                    )
    # list_filter = ('classe',)
    # search_fields = ('nom', 'prenom', 'classe')
    ordering = ('nom', 'prenom')
    filter_horizontal = ()
