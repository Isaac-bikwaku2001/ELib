from rest_framework import serializers
from elibrary.models import *

class AuteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auteur
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class LivreSerializer(serializers.ModelSerializer):
    auteur = AuteurSerializer()
    genre = GenreSerializer()
    class Meta:
        model = Livre
        fields = '__all__'

class ExemplaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exemplaire
        fields = '__all__'

class EmpruntSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprunt
        fields = '__all__'