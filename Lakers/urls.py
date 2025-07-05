from django.urls import path
from . import views

urlpatterns = [
path("", views.index, name="index"),
path("elenco/", views.jogadores, name="jogadores"),
path("sobre/", views.sobre, name="sobre"),
]