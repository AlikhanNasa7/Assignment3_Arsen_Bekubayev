from django.shortcuts import render, redirect, get_object_or_404
from .models import Specialize
from health_forms.forms import SpecializeForm


def specialize_list(request):
    specializes = Specialize.objects.all()
    return render(request, 'specializes/index.html', {'specializes': specializes, 'heading': 'Specializes'})


def create_specialize(request):
    if request.method == 'POST':
        form = SpecializeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('specialize-list')
    else:
        form = SpecializeForm()
    return render(request, 'specializes/specializes_form.html', {'form': form, 'heading': 'Create Specialize'})


def update_specialize(request, pk):
    specialize = Specialize.objects.filter(diseasetype=pk).first()
    if request.method == 'POST':
        form = SpecializeForm(request.POST, instance=specialize)
        if form.is_valid():
            form.save()
            return redirect('specialize-list')
    else:
        form = SpecializeForm(instance=specialize)
    return render(request, 'specializes/specializes_form.html', {'form': form, 'heading': 'Update Specialize'})


def delete_specialize(request, pk):
    specialize = Specialize.objects.filter(diseasetype=pk).first()
    if request.method == 'POST':
        specialize.delete()
    return redirect('specialize-list')