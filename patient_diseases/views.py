from django.shortcuts import render, redirect, get_object_or_404
from .models import Patientdisease
from health_forms.forms import PatientDiseaseForm


def patientdisease_list(request):
    patientdiseases = Patientdisease.objects.all()
    return render(request, 'patient_diseases/index.html', {'patientdiseases': patientdiseases, 'heading': 'Patient Diseases'})


def create_patientdisease(request):
    if request.method == 'POST':
        form = PatientDiseaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patientdisease-list')
    else:
        form = PatientDiseaseForm()
    return render(request, 'patient_diseases/patient_diseases_form.html', {'form': form, 'heading': 'Create Patient Disease'})


def update_patientdisease(request, pk):
    patientdisease = get_object_or_404(Patientdisease, pk=pk)
    if request.method == 'POST':
        form = PatientDiseaseForm(request.POST, instance=patientdisease)
        if form.is_valid():
            form.save()
            return redirect('patientdisease-list')
    else:
        form = PatientDiseaseForm(instance=patientdisease)
    return render(request, 'patient_diseases/patient_diseases_form.html', {'form': form, 'heading': 'Update Patient Disease'})


def delete_patientdisease(request, pk):
    patientdisease = get_object_or_404(Patientdisease, pk=pk)
    if request.method == 'POST':
        patientdisease.delete()
    return redirect('patientdisease-list')
