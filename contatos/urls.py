from django.urls import path
from . import views

app_name = 'contatos'

urlpatterns = [
    path('', views.ContatoListView.as_view(), name='listar'),
    path('<int:pk>/', views.ContatoDetailView.as_view(), name='detalhar'),
    path('novo/', views.ContatoCreateView.as_view(), name='criar'),
    path('<int:pk>/editar/', views.ContatoUpdateView.as_view(), name='editar'),
    path('<int:pk>/deletar/', views.ContatoDeleteView.as_view(), name='deletar'),
]