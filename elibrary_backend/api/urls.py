from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAuteur),
    path('genres/', views.getGenre),
    path('livres/', views.getLivre),
    path('exemplaires/', views.getExemplaire),
    path('emprunts/', views.getEmprunt),
    path('livres/<int:id>/', views.detailView.as_view(), name="detail")
]