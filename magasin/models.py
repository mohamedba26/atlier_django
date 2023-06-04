from django.db import models
from datetime import date
# Create your models here.
class produit(models.Model):
    TYPE_CHOICES=[('em','emballé'),('fr','Frais'),('cs','Conserve')]
    libelle=models.CharField(max_length=25)
    description=models.TextField(default='Non définie')
    prix=models.DecimalField(max_digits=10,decimal_places=3)
    type=models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    img=models.ImageField(blank=True)
    categorie=models.ForeignKey('Categorie',on_delete=models.CASCADE,null=True)
    fournisseur=models.ForeignKey('Fournisseur',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.libelle+" "+self.description+" "+str(self.prix)
class Categorie(models.Model):
    TYPE_CHOICES=[('Al','Alimentaire'),('Mb','Meuble'),('Sn','Sanitaire'),('Vs','Vaisselle'),('Vt','Vêtement'),('Jx','Jouets'),('Lg','Linge de Maison'),('Bj','Bijoux'),('Dc','Décor')]
    name=models.CharField(max_length=2,choices=TYPE_CHOICES,default='Al')
    def __str__(self):
        return self.name
class Fournisseur(models.Model):
    name=models.CharField(max_length=100)
    adress=models.TextField()
    email=models.EmailField()
    telephone=models.CharField(max_length=8)
    def __str__(self):
        return self.name
class ProduitNC(produit):
    Duree_garantie=models.CharField(max_length=100)
    def __str__(self):
            return super().__str__()+" "+self.Duree_garantie
class Commande(models.Model):
    dateCde=models.DateField(null=True,default=date.today)
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    produits=models.ManyToManyField('Produit')
    def __str__(self):
        return str(self.dateCde)+" "+str(self.totalCde)