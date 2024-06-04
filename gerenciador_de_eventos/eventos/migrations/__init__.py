from django.urls import path
from . import views.py

urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),