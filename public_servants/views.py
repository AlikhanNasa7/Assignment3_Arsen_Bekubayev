from django.shortcuts import render, redirect, get_object_or_404
from .models import Publicservant
from health_forms.forms import PublicServantForm


def servant_list(request):
    servants = Publicservant.objects.all()
    return render(request, 'public_servants/index.html', {'servants': servants, 'heading': 'Public Servants'})


def create_servant(request):
    if request.method == 'POST':
        form = PublicServantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servant-list')
    else:
        form = PublicServantForm()
    return render(request, 'public_servants/public_servants_form.html', {'form': form, 'heading': 'Create Public Servant'})


def update_servant(request, pk):
    servant = get_object_or_404(Publicservant, pk=pk)
    if request.method == 'POST':
        form = PublicServantForm(request.POST, instance=servant)
        if form.is_valid():
            form.save()
            return redirect('servant-list')
    else:
        form = PublicServantForm(instance=servant)
    return render(request, 'public_servants/public_servants_form.html', {'form': form, 'heading': 'Update Servant'})


def delete_servant(request, pk):
    servant = get_object_or_404(Publicservant, pk=pk)
    if request.method == 'POST':
        servant.delete()
    return redirect('servant-list')