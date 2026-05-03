from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistroUsuarioForm


def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('lista_servicios')
    else:
        form = RegistroUsuarioForm()

    return render(request, 'users/registro.html', {'form': form})