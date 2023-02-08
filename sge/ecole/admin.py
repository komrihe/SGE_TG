from django.contrib import admin
from .models import Programme, Classe
# Register your models here.
@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'duree', 'montant')

@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'programme')
