from django.shortcuts import render, get_object_or_404, redirect
from .models import Vaga
from .forms import MenuForm

def menu_principal(request):
    form = MenuForm()
    return render(request, 'estacionamento/menu_principal.html', {'form': form})

def lista_vagas(request):
    vagas = Vaga.objects.all()
    return render(request, 'estacionamento/lista_vagas.html', {'vagas': vagas})

def detalhe_vaga(request, pk):
    vaga = get_object_or_404(Vaga, pk=pk)
    return render(request, 'estacionamento/detalhe_vaga.html', {'vaga': vaga})

def editar_vaga(request, pk):
     vaga = get_object_or_404(Vaga, pk=pk)
     if request.method == "POST":
         form = MenuForm(request.POST, instance=vaga)
         if form.is_valid():
             vaga = form.save()
             return redirect('lista_vagas')
     else:
         form = MenuForm(instance=vaga)
     return render(request, 'estacionamento/editar_vaga.html', {'form': form})