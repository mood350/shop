from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import *
from .forms import *
from django.db.models import Count, Sum, F
from datetime import datetime, timedelta
from django.utils import timezone
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.db.models.functions import TruncMonth
today = timezone.now()
from django.http import JsonResponse
# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def article(request):
    articles = Article.objects.all()
    return render(request, 'article.html', {'articles': articles})

@login_required
def client(request):
    clients = Client.objects.all()
    return render(request, 'client.html', {'clients': clients})

@login_required
def categorie(request):
    categories = Categorie.objects.all()
    return render(request, 'categorie.html', {'categories': categories})

@login_required
def vente(request):
    ventes = Ventes.objects.all()
    return render(request, 'vente.html', {'ventes': ventes})


def facture(request):
    factures = Facture.objects.all()
    return render(request, 'facture.html', {'factures': factures})

@login_required
def ajouter_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('article')
    else:
        form = ArticleForm()
    return render(request, 'ajouter_article.html', {'form': form})

@login_required
def ajouter_categorie(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorie')
    else:
        form = CategorieForm()
    return render(request, 'ajouter_categorie.html', {'form': form})

@login_required
def ajouter_vente(request):
    if request.method == 'POST':
        form = VentesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vente')
    else:
        form = VentesForm()
    return render(request, 'ajouter_vente.html', {'form': form})

@login_required
def ajouter_Facture(request):
    if request.method == 'POST':
        form = FactureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facture')
    else:
        form = FactureForm()
    return render(request, 'ajouter_Facture.html', {'form': form})

@login_required
def ajouter_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client')
    else:
        form = ClientForm()
    return render(request, 'ajouter_client.html', {'form': form})

def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('acceuil')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'connexion.html')

@login_required
def modifier_vente(request, id):
    vente = get_object_or_404(Ventes, id=id)
    if request.method == 'POST':
        form = VentesForm(request.POST, instance=vente)
        if form.is_valid():
            form.save()
            return redirect('vente')
    else:
        form = VentesForm(instance=vente)
    return render(request, 'modifier_vente.html', {'form': form})

@login_required
def modifier_article(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'modifier_article.html', {'form': form})

@login_required
def modifier_client(request, id):
    client = get_object_or_404(Client, id=id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client')
    else:
        form = ClientForm(instance=client)
    return render(request, 'modifier_client.html', {'form': form})

@login_required
def modifier_categorie(request, id):
    categorie = get_object_or_404(Categorie, id=id)
    if request.method == 'POST':
        form = CategorieForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            return redirect('categorie')
    else:
        form = CategorieForm(instance=categorie)
    return render(request, 'modifier_categorie.html', {'form': form})

@login_required
def supprimer_vente(request, id):
    vente = get_object_or_404(Ventes, id=id)
    if request.method == 'POST':  # Si le formulaire de confirmation est soumis
        vente.delete()
        messages.success(request, 'Vente supprimée avec succès!')
        return redirect('vente')  # Redirige vers la liste des ventes
    return render(request, 'supprimer_vente.html', {'vente': vente})

@login_required
def supprimer_article(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':  # Si le formulaire de confirmation est soumis
        vente.delete()
        messages.success(request, 'Article supprimé avec succès!')
        return redirect('article')  # Redirige vers la liste des ventes
    return render(request, 'supprimer_article.html', {'article': article})

@login_required
def supprimer_client(request, id):
    client = get_object_or_404(Client, id=id)
    if request.method == 'POST':  # Si le formulaire de confirmation est soumis
        client.delete()
        messages.success(request, 'Client supprimé avec succès!')
        return redirect('client')  # Redirige vers la liste des clients
    return render(request, 'supprimer_client.html', {'client': client})

@login_required
def supprimer_categorie(request, id):
    categorie = get_object_or_404(Categorie, id=id)
    if request.method == 'POST':  # Si le formulaire de confirmation est soumis
        categorie.delete()
        messages.success(request, 'Catégorie supprimée avec succès!')
        return redirect('categorie')  # Redirige vers la liste des catégories
    return render(request, 'supprimer_categorie.html', {'categorie': categorie})

@login_required
def supprimer_Facture(request, id):
    facture = get_object_or_404(Facture, id=id)
    if request.method == 'POST':  # Si le formulaire de confirmation est soumis
        facture.delete()
        messages.success(request, 'Facture supprimée avec succès!')
        return redirect('facture')  # Redirige vers la liste des factures
    return render(request, 'supprimer_Facture.html', {'facture': facture})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def modifier_Facture(request, id):
    facture = get_object_or_404(Facture, id=id)
    if request.method == 'POST':
        form = FactureForm(request.POST, instance=facture)
        if form.is_valid():
            form.save()
            return redirect('facture')
    else:
        form = FactureForm(instance=facture)
    return render(request, 'modifier_Facture.html', {'form': form})

@login_required
def acceuil(request):
    return render(request, 'acceuil.html')

def deconnexion(request):
    logout(request)
    return redirect('connexion')

@login_required
def facture_details(request, id):
    facture = get_object_or_404(Facture, id=id)  # Récupère la facture par ID ou affiche une erreur 404
    return render(request, 'facture_details.html', {'facture': facture})

@login_required
def supprimer_vente(request, id):
    vente = get_object_or_404(Ventes, id=id)
    if request.method == 'POST':  # Si le formulaire de confirmation est soumis
        vente.delete()
        messages.success(request, 'Vente supprimée avec succès!')
        return redirect('vente')
    return render(request, 'supprimer_vente.html', {'vente': vente})

@login_required
def dashboard(request):
    # Obtenir la période de filtrage
    periode = request.GET.get('periode', 'aujourdhui')
    maintenant = timezone.now()

    # Filtrage par période
    if periode == 'aujourdhui':
        ventes = Ventes.objects.filter(date_vente__date=maintenant.date())
    elif periode == 'semaine':
        debut_semaine = maintenant - timedelta(days=maintenant.weekday())
        ventes = Ventes.objects.filter(date_vente__date__gte=debut_semaine.date())
    elif periode == 'mois':
        ventes = Ventes.objects.filter(date_vente__year=maintenant.year, date_vente__month=maintenant.month)
    elif periode == 'annee':
        ventes = Ventes.objects.filter(date_vente__year=maintenant.year)
    else:
        ventes = Ventes.objects.all()

    # Calculs
    total_ventes = ventes.count()
    revenu_total = ventes.aggregate(revenu=Sum(F('prix_total')))['revenu'] or 0

    # Articles les plus vendus
    articles_populaires = list(ventes.values('article__nom').annotate(total=Sum('quantite_achetee')).order_by('-total')[:5])

    # Ventes par mois
    ventes_par_mois = list(Ventes.objects.filter(date_vente__year=maintenant.year).values('date_vente__month').annotate(total=Count('id')).order_by('date_vente__month'))

    # Préparer le contexte
    context = {
        'total_ventes': total_ventes,
        'revenu_total': revenu_total,
        'articles_populaires': articles_populaires,
        'ventes_par_mois': ventes_par_mois,
        'periode': periode,
    }

    # Retourner une réponse JSON si la requête est AJAX
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse(context)
    else:
        return render(request, 'dashboard.html', context)

def recherche_article(request):
    form = RechercheArticleForm(request.GET or None)  # Utilisation de GET au lieu de POST
    articles = Article.objects.all()  # On commence par tous les articles

    if form.is_valid():
        nom = form.cleaned_data['nom']
        if nom:
            articles = articles.filter(nom__icontains=nom)
        
        tri = request.GET.get('tri', 'nom')
        if tri == 'nom':
            articles = articles.order_by('nom')
        elif tri == 'prix_croissant':
            articles = articles.order_by('prix')
        elif tri == 'prix_decroissant':
            articles = articles.order_by('-prix')
        elif tri == 'stock':
            articles = articles.order_by('-stock')

        return render(request, 'recherche_article.html', {
            'form': form,
            'articles': articles,
            'tri': tri  # On passe l'option de tri au template
        })