from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from elibrary.models import *
from .serializers import *
from rest_framework import status
from django.contrib.auth import authenticate, login, logout

# API ACTEUR
@api_view(['GET'])
def getAuteur(request):
    auteurs = Auteur.objects.all()
    serializer = AuteurSerializer(auteurs, many=True)
    return Response(serializer.data)

# API GENRE
@api_view(['GET'])
def getGenre(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

# API LIVRE
@api_view(['GET'])
def getLivre(request):
    livres = Livre.objects.all()
    serializer = LivreSerializer(livres, many=True)
    return Response(serializer.data)

# API EXEMPLAIRE
@api_view(['GET'])
def getExemplaire(request):
    exemplaires = Exemplaire.objects.all()
    serializer = ExemplaireSerializer(exemplaires, many=True)
    return Response(serializer.data)

# API EMPRUNT
@api_view(['GET'])
def getEmprunt(request):
    emprunts = Emprunt.objects.all()
    serializer = EmpruntSerializer(emprunts, many=True)
    return Response(serializer.data)

class detailView(APIView):
    def get(self, request, id):
        try:
            livre = Livre.objects.get(id=id)
            serializer = LivreSerializer(livre)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

class CreateUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
    
# @api_view(['POST'])
# def add(request):
#     serializer = AuteurSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
