from django.db import models
# Create your models here.

class Client(models.Model):
    nom = models.CharField(max_length=100)
    prenoms = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)

class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=100)

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
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantite_achetee = models.PositiveIntegerField()
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

        #nom de l'article
        self.article_nom = self.article.nom
        self.prix = self.article.prix
        super().save(*args, **kwargs)

    def __str__(self):
        return self.article.nom
    
class Facture(models.Model):
    id_facture = models.IntegerField()
    id_vente = models.ForeignKey(Ventes, on_delete=models.CASCADE)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    #le prix total est inmodifiable manuellement
    prix_total = models.FloatField(editable=False)
    nom_client = models.CharField(max_length=100)
    date_Facture = models.DateTimeField(auto_now_add=True, blank=True)

    #Rempli la section prix total via l'id de la vente
    def save(self, *args, **kwargs):
        prix_total = self.id_vente.prix_total
        nom_client = self.id_client.nom
        super().save(*args, **kwargs)

class Stock_article(models.Model):
    article = models.OneToOneField(Article, on_delete=models.CASCADE)
    stock_article = models.PositiveIntegerField(editable=False)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.stock_article = self.article.stock
        super().save(*args, **kwargs)