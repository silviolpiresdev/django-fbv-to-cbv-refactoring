from django.shortcuts import render, redirect, get_object_or_404
from .models import Contato
from .forms import ContatoForm


def listar_contatos(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/lista.html', {'contatos': contatos})


def detalhar_contato(request, pk):
    contato = get_object_or_404(Contato, pk=pk)
    return render(request, 'contatos/detalhe.html', {'contato': contato})


def criar_contato(request):
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('contatos:listar')
    return render(request, 'contatos/form.html', {'form': form, 'page_title': 'Novo Contato'})


def editar_contato(request, pk):
    contato = get_object_or_404(Contato, pk=pk)
    form = ContatoForm(request.POST or None, instance=contato)
    if form.is_valid():
        form.save()
        return redirect('contatos:listar')
    return render(request, 'contatos/form.html', {'form': form, 'page_title': 'Editar Contato'})


def deletar_contato(request, pk):
    contato = get_object_or_404(Contato, pk=pk)
    if request.method == 'POST':
        contato.delete()
        return redirect('contatos:listar')
    return render(request, 'contatos/confirmar_delete.html', {'contato': contato})