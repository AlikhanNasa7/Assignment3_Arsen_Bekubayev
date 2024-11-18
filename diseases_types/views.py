from django.shortcuts import render, redirect, get_object_or_404
from .models import Diseasetype
from health_forms.forms import DiseaseTypeForm


def diseasetype_list(request):
    disease_types = Diseasetype.objects.all()
    return render(request, 'diseases_types/index.html', {'disease_types': disease_types, 'heading': 'Disease Types'})


def create_diseasetype(request):
    if request.method == 'POST':
        form = DiseaseTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('discovery-list')
    else:
        form = DiseaseTypeForm()
    return render(request, 'diseases_types/diseases_types_form.html', {'form': form, 'heading': 'Create Disease'})


def update_diseasetype(request, pk):
    diseasetype = get_object_or_404(Diseasetype, pk=pk)
    if request.method == 'POST':
        form = DiseaseTypeForm(request.POST, instance=diseasetype)
        if form.is_valid():
            form.save()
            return redirect('diseases_types-list')
    else:
        form = DiseaseTypeForm(instance=diseasetype)
    return render(request, 'diseases_types/diseases_types_form.html', {'form': form})


def delete_diseasetype(request, pk):
    discover = get_object_or_404(Diseasetype, pk=pk)
    if request.method == 'POST':
        discover.delete()
    return redirect('diseases-list')
