from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('index/', login_required(views.acceuil), name='index'),
    path('article/', login_required(views.article), name='article'),
    path('client/', views.client, name='client'),
    path('categorie/', views.categorie, name='categorie'),
    path('vente/', views.vente, name='vente'),
    path('facture/', views.facture, name='facture'),
    path('ajouter_article/', views.ajouter_article, name='ajouter_article'),
    path('ajouter_categorie/', views.ajouter_categorie, name='ajouter_categorie'),
    path('ajouter_vente/', views.ajouter_vente, name='ajouter_vente'),
    path('ajouter_Facture/', views.ajouter_Facture, name='ajouter_Facture'),
    path('ajouter_client/', views.ajouter_client, name='ajouter_client'),
    path('inscription/', views.inscription, name='inscription'),
    path('', views.connexion, name='connexion'),
    path('acceuil/', views.acceuil, name='acceuil'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('modifier_vente/<int:id>/', views.modifier_vente, name='modifier_vente'),
    path('modifier_article/<int:id>/', views.modifier_article, name='modifier_article'),
    path('modifier_categorie/<int:id>/', views.modifier_categorie, name='modifier_categorie'),
    path('modifier_client/<int:id>/', views.modifier_client, name='modifier_client'),
    path('supprimer_article/<int:id>/', views.supprimer_article, name='supprimer_article'),
    path('supprimer_categorie/<int:id>/', views.supprimer_categorie, name='supprimer_categorie'),
    path('supprimer_client/<int:id>/', views.supprimer_client, name='supprimer_client'),
    path('supprimer_vente/<int:id>/', views.supprimer_vente, name='supprimer_vente'),
    path('supprimer_Facture/<int:id>/', views.supprimer_Facture, name='supprimer_Facture'),
    path('modifier_Facture/<int:id>/', views.modifier_Facture, name='modifier_Facture'),
    path('facture/<int:id>/', views.facture_details, name='facture_details'),
    path('article/', views.recherche_article, name='recherche_article'),
    path('dashboard/', views.dashboard, name='dashboard'),
]