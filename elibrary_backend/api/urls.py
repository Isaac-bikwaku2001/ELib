from django.urls import path
from . import views
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('', views.getAuteur),
    path('genres/', views.getGenre),
    path('livres/', views.getLivre),
    path('exemplaires/', views.getExemplaire),
    path('emprunts/', views.getEmprunt),
    path('livres/<int:id>/', views.detailView.as_view(), name="detail"),
    path('api-token-auth/', ObtainAuthToken.as_view()),
    path('login/register/', views.CreateUserView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
]