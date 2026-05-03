from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Servicio
from .forms import ServicioForm


def lista_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'events/lista_servicios.html', {'servicios': servicios})


@login_required
def crear_servicio(request):
    if not request.user.es_proveedor:
        return redirect('lista_servicios')

    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            servicio = form.save(commit=False)
            servicio.proveedor = request.user
            servicio.save()
            return redirect('lista_servicios')
    else:
        form = ServicioForm()

    return render(request, 'events/crear_servicio.html', {'form': form})