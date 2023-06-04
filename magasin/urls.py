from django.urls import path,include
from .views import CategoryAPIView,ProductAPIView
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('produits/',views.myProducts,name='produits'),
    path('fournisseur/',views.nouveauFournisseur,name='nouveauFour'),
    path('commande/',views.nouveauCommande,name='nouveauCommande'),
    path('register/',views.register, name = 'register'),
    path('home/',views.home, name = 'home'),
    path('api/category/', CategoryAPIView.as_view()),
    path('api/product/', ProductAPIView.as_view()),
]