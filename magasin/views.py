from .models import produit,Fournisseur,Categorie,Commande
from django.shortcuts import redirect,render
from django.http import HttpResponseRedirect
from .forms import ProduitForm, FournisseurForm,CommandeForm,UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CategorySerializer,ProduitSerializer
from rest_framework import viewsets

@login_required
def index(request):
    list=produit.objects.all()
    return render(request,'magasin/vitrine.html',{'list':list})

@login_required
def myProducts(request):
    products = produit.objects.all()
    context={'products':products}
    return render( request,'magasin/mesProduits.html',context)

@login_required
def nouveauFournisseur(request):
    if request.method == "POST" :
        form = FournisseurForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin')
    else :
        form = FournisseurForm()
    list=Fournisseur.objects.all()
    return render(request,'magasin/fournisseur.html',{'list':list,'form':form})

@login_required
def nouveauCommande(request):
    if request.method == "POST" :
        form = CommandeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin')
    else :
        form = CommandeForm()
    list=Commande.objects.all()
    return render(request,'magasin/commande.html',{'list':list,'form':form}) 
@login_required
def home(request):
    context={'val':"Menu Acceuil"}
    return HttpResponseRedirect('/magasin')
def register(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request,'registration/registration.html',{'form' : form})

class CategoryAPIView(APIView):
        def get(self, *args, **kwargs):
            categories = Categorie.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data)
class ProductAPIView(APIView):
        def get(self, *args, **kwargs):
            produits = produit.objects.all()
            serializer = ProduitSerializer(produits, many=True)
            return Response(serializer.data)

class ProductViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProduitSerializer
    def get_queryset(self):
        queryset = produit.objects.filter()
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(categorie_id=category_id)
        return queryset