from django.urls import path
from django.urls.resolvers import URLPattern

# on appelle les views créées dans le views.py
from .views import getJoueurs, getOneJoueur #, example_view

urlpatterns = [
    path('joueurs/', getJoueurs, name="getJoueurs"),
    path('joueur/<int:pk>/', getOneJoueur, name="getOneJoueur"),
    #path('example/', example_view, name="example_view"),
]