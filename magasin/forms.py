from django.forms import ModelForm
from .models import produit,Commande,Fournisseur
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class ProduitForm(ModelForm):
    class Meta :
        model = produit
        fields = "__all__"
class FournisseurForm(ModelForm):
    class Meta :
        model = Fournisseur
        fields = "__all__"
class CommandeForm(ModelForm):
    class Meta:
        model=Commande
        fields=['totalCde','produits']
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')

class Meta(UserCreationForm.Meta):
    model = User
    fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')