from django.contrib import admin
from .models import *
# Register your models here.

class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom_categorie',)
admin.site.register(Categorie, CategorieAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('nom', 'stock', 'prix')
    list_filter = ('prix',)
admin.site.register(Article, ArticleAdmin)

class FactureAdmin(admin.ModelAdmin):
    list_display = ('client', 'prix_total', 'date_Facture')
    list_filter = ('date_Facture',)
admin.site.register(Facture, FactureAdmin)

class VentesAdmin(admin.ModelAdmin):
    list_display = ('article', 'quantite_achetee', 'prix', 'prix_total', 'payement', 'date_vente')
    list_filter = ('date_vente',)
admin.site.register(Ventes, VentesAdmin)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenoms', 'telephone')

admin.site.register(Client, ClientAdmin)
