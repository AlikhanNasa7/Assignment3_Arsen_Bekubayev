from django.shortcuts import render, redirect, get_object_or_404
from .models import Disease
from health_forms.forms import DiseaseForm


def disease_list(request):
    diseases = Disease.objects.all()
    return render(request, 'diseases/index.html', {'diseases': diseases, 'heading': 'Diseases'})


def create_disease(request):
    if request.method == 'POST':
        form = DiseaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('discovery-list')
    else:
        form = DiseaseForm()
    return render(request, 'diseases/diseases_form.html', {'form': form, 'heading': 'Create Disease'})


def update_disease(request, pk):
    discover = get_object_or_404(Disease, pk=pk)
    if request.method == 'POST':
        form = DiseaseForm(request.POST, instance=discover)
        if form.is_valid():
            form.save()
            return redirect('diseases-list')
    else:
        form = DiseaseForm(instance=discover)
    return render(request, 'diseases/diseases_form.html', {'form': form})


def delete_disease(request, pk):
    discover = get_object_or_404(Disease, pk=pk)
    if request.method == 'POST':
        discover.delete()
    return redirect('diseases-list')
