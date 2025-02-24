from django.db import models

# Create your models here.

MOYEN_PAIEMENT_CHOIX = [
        ('CASH', 'Espèces'),
        ('TMONEY', 'Tmoney'),
        ('FLOOZ', 'Flooz'),
    ]

class Utilisateur(models.Model):
    nom = models.CharField(max_length=50)  
    mot_de_passe = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

class Client(models.Model):
    nom = models.CharField(max_length=100)
    prenoms = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} {self.prenoms}"

class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom_categorie

class Article(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(null=True)
    prix = models.FloatField()

    def __str__(self):
        return self.nom

class Ventes(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    quantite_achetee = models.PositiveIntegerField()
    payement = models.CharField(max_length=100, choices=MOYEN_PAIEMENT_CHOIX, default='CASH')
    prix = models.FloatField(editable=False)
    prix_total = models.FloatField(editable=False)
    date_vente = models.DateTimeField(auto_now_add=True)
 
    def save(self, *args, **kwargs):
        # Calcul du prix total
        self.prix = self.article.prix
        self.prix_total = self.quantite_achetee * self.article.prix

        # Vérification du stock
        if self.article.stock < self.quantite_achetee:
            raise ValueError("Stock insuffisant pour cet article.")

        # Mise à jour du stock
        self.article.stock -= self.quantite_achetee
        self.article.save()

        super().save(*args, **kwargs)

        # Création automatique d'une facture
        Facture.objects.create(
            vente=self,
            client=self.client,
            article=self.article,
            quantite=self.quantite_achetee,
            prix=self.prix,
            prix_total=self.prix_total
        )

    def __str__(self):
        return f"Vente de {self.article.nom} - {self.quantite_achetee} unités"
    
class Facture(models.Model):
    vente = models.OneToOneField(Ventes, on_delete=models.CASCADE, null=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    quantite = models.IntegerField(default=1)
    nom_article = models.CharField(max_length=100, null=True, editable=False)
    prix = models.FloatField(editable=False)
    prix_total = models.FloatField(editable=False)
    date_Facture = models.DateTimeField(auto_now_add=True, blank=True)

    def save(self, *args, **kwargs):
        # Récupère le nom de l'article
        if self.article:
            self.nom_article = self.article.nom

        # Calcule le prix total
        self.prix_total = self.prix * self.quantite

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Facture pour {self.nom_article} - {self.quantite} unités"
