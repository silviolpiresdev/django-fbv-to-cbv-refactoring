from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Contato
from .forms import ContatoForm


class ContatoListView(ListView):
    model = Contato
    template_name = 'contatos/lista.html'
    context_object_name = 'contatos'


class ContatoDetailView(DetailView):
    model = Contato
    template_name = 'contatos/detalhe.html'
    context_object_name = 'contato'


class ContatoCreateView(CreateView):
    model = Contato
    form_class = ContatoForm
    template_name = 'contatos/form.html'
    success_url = reverse_lazy('contatos:listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Novo Contato'
        return context


class ContatoUpdateView(UpdateView):
    model = Contato
    form_class = ContatoForm
    template_name = 'contatos/form.html'
    success_url = reverse_lazy('contatos:listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Editar Contato'
        return context


class ContatoDeleteView(DeleteView):
    model = Contato
    template_name = 'contatos/confirmar_delete.html'
    success_url = reverse_lazy('contatos:listar')
    context_object_name = 'contato'