from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),
    path('<int:evento_id>/', views.detalhe_evento, name='detalhe_evento'),
    path('novo/', views.novo_evento, name='novo_evento'),
    path('editar/<int:evento_id>/', views.editar_evento, name='editar_evento'),
    path('deletar/<int:evento_id>/', views.deletar_evento, name='deletar_evento'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('eventos/', include('eventos.urls')),
]