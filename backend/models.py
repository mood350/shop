from django.db import models
# Create your models here.

class Utilisateur(models.Model):
    nom = models.CharField(max_length=50)  
    mot_de_passe = models.CharField(max_length=50)


class Client(models.Model):
    nom = models.CharField(max_length=100)
    prenoms = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)

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
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantite_achetee = models.PositiveIntegerField()
    prix = models.FloatField(editable=False)
    prix_total = models.FloatField(editable=False)
    date_vente = models.DateTimeField(auto_now_add=True)
    article_nom = models.CharField(null=True)
 
    def save(self, *args, **kwargs):
        # Calcul du prix total
        self.prix = self.article.prix
        self.prix_total = self.quantite_achetee * self.article.prix
        self.article_nom = self.article.nom

        # Vérification du stock
        if self.article.stock < self.quantite_achetee:
            raise ValueError("Stock insuffisant pour cet article.")

        # Mise à jour du stock
        self.article.stock -= self.quantite_achetee
        self.article.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.article.nom
    
class Facture(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    client = models.CharField(max_length=100, null=True)
    quantite = models.IntegerField(default=1)
    nom_article = models.CharField(max_length=100, null=True, editable=False)
    prix = models.FloatField(editable=False)
    #le prix total est inmodifiable manuellement
    prix_total = models.FloatField(editable=False)
    date_Facture = models.DateTimeField(auto_now_add=True, blank=True)

    #Rempli la section prix total via l'id de la vente
    def save(self, *args, **kwargs):
    # Récupère le nom et le prix de l'article lié
        if self.article:
            self.nom_article = self.article.nom
            self.prix = self.article.prix
        else:
            self.nom_article = ""
            self.prix = 0
            
        # Calcule le prix total seulement si prix et quantité sont définis
        if self.prix is not None and self.quantite is not None:
            self.prix_total = self.prix * self.quantite
        else:
            self.prix_total = 0

        # Appelle la méthode save de la classe parente
        super().save(*args, **kwargs)
