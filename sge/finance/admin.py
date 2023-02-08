from django.contrib import admin
from .models import CompteAPayer
# Register your models here.
@admin.register(CompteAPayer)
class CompteAPayerAdmin(admin.ModelAdmin):
    list_display = ('eleve', 'montant_a_payer',)
    list_filter = (
        # 'statut', 
        # 'date'
        )
    search_fields = ('eleve', 'montant', )
    # date_hierarchy = 'date'
    # ordering = ('date',)