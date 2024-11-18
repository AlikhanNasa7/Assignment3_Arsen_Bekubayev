from django.shortcuts import render, redirect, get_object_or_404
from .models import Record
from health_forms.forms import RecordForm


def record_list(request):
    records = Record.objects.all()
    return render(request, 'records/index.html', {'records': records, 'heading': 'Records'})


def create_record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('record-list')
    else:
        form = RecordForm()
    return render(request, 'records/records_form.html', {'form': form, 'heading': 'Create Record'})


def update_record(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('record-list')
    else:
        form = RecordForm(instance=record)
    return render(request, 'records/records_form.html', {'form': form, 'heading': 'Update Record'})


def delete_record(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        record.delete()
    return redirect('record-list')