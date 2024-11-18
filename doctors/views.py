from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor
from health_forms.forms import DoctorForm


def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/index.html', {'doctors': doctors, 'heading': 'Doctors'})


def create_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor-list')
    else:
        form = DoctorForm()
    return render(request, 'doctors/doctors_form.html', {'form': form, 'heading': 'Create Doctor'})


def update_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor-list')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctors/doctors_form.html', {'form': form, 'heading': 'Update Doctor'})


def delete_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
    return redirect('doctor-list')
