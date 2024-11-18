from django.shortcuts import render, redirect, get_object_or_404
from .models import Patients
from health_forms.forms import PatientForm


def patient_list(request):
    patients = Patients.objects.all()
    return render(request, 'patients/index.html', {'patients': patients, 'heading': 'Patients'})


def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient-list')
    else:
        form = PatientForm()
    return render(request, 'patients/patients_form.html', {'form': form, 'heading': 'Create Patient'})


def update_patient(request, pk):
    patient = get_object_or_404(Patients, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient-list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patients/patients_form.html', {'form': form, 'heading': 'Update Patient'})


def delete_patient(request, pk):
    patient = get_object_or_404(Patients, pk=pk)
    if request.method == 'POST':
        patient.delete()
    return redirect('patient-list')
