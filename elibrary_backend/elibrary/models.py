from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Auteur(models.Model):
    nom = models.CharField(max_length=100, null=False)
    prenom = models.CharField(max_length=100, null=False)
    nationalite = models.CharField(max_length=80, null=False)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Genre(models.Model):
    libelle = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.libelle

class Livre(models.Model):
    ISBN = models.CharField(max_length=50, unique=True, null=False)
    titre = models.CharField(max_length=90, null=False)
    langue = models.CharField(max_length=50, null=False)
    date_edition = models.DateField()
    image = models.ImageField(null=True, blank=True)
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre

class Exemplaire(models.Model):
    nombre_exemplaire = models.IntegerField()
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "N° exemplaire: " + str(self.nombre_exemplaire) + " " + "Titre: "+ self.livre.titre

class Emprunt(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    date_emprunt = models.DateField(auto_now_add=True)
    date_remise = models.DateField(default=date.today().day + 5)