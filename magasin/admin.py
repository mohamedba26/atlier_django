from django.contrib import admin
from .models import produit,Categorie,Fournisseur,ProduitNC,Commande
# Register your models here.
admin.site.register(produit)
admin.site.register(Categorie)
admin.site.register(Fournisseur)
admin.site.register(ProduitNC)
admin.site.register(Commande)
