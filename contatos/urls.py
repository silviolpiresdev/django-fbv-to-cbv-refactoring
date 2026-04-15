from django.urls import path
from . import views

app_name = 'contatos'

urlpatterns = [
    path('', views.listar_contatos, name='listar'),
    path('<int:pk>/', views.detalhar_contato, name='detalhar'),
    path('novo/', views.criar_contato, name='criar'),
    path('<int:pk>/editar/', views.editar_contato, name='editar'),
    path('<int:pk>/deletar/', views.deletar_contato, name='deletar'),
]