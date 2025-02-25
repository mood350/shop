from django import forms
from .models import Client, Categorie, Article, Ventes, Facture
from django.contrib.auth.forms import UserCreationForm

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom', 'prenoms', 'telephone']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'prenoms': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénoms'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'}),
        }

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['nom_categorie']
        widgets = {
            'nom_categorie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la catégorie'}),
        }

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['categorie', 'nom', 'stock', 'prix']
        widgets = {
            'categorie': forms.Select(attrs={'class': 'form-select'}),
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de l\'article'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Stock disponible'}),
            'prix': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Prix unitaire'}),
        }

class VentesForm(forms.ModelForm):
    class Meta:
        model = Ventes
        fields = ['article', 'client', 'quantite_achetee', 'payement']
        widgets = {
            'article': forms.Select(attrs={'class': 'form-select'}),
            'client': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Nom du client'}),
            'quantite_achetee': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantité achetée'}),
            'payement': forms.Select(attrs={'class': 'form-select'}),
        }

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['client', 'article', 'quantite']
        widgets = {
            'client': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du client'}),
            'article': forms.Select(attrs={'class': 'form-select'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantité'}),
        }

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("password1", "password2")

class RechercheArticleForm(forms.Form):

    nom = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de l\'article'})
    )