from django.shortcuts import render, redirect, get_object_or_404
from .models import Discover
from health_forms.forms import DiscoverForm


def discovery_list(request):
    discoveries = Discover.objects.all()
    return render(request, 'discoveries/index.html', {'discoveries': discoveries, 'heading': 'Discoveries'})


def create_discovery(request):
    if request.method == 'POST':
        form = DiscoverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('discovery-list')
    else:
        form = DiscoverForm()
    return render(request, 'discoveries/discovery_form.html', {'form': form, 'heading': 'Create Discovery'})


def update_discovery(request, pk):
    discover = get_object_or_404(Discover, pk=pk)
    if request.method == 'POST':
        form = DiscoverForm(request.POST, instance=discover)
        if form.is_valid():
            form.save()
            return redirect('discovery-list')
    else:
        form = DiscoverForm(instance=discover)
    return render(request, 'discoveries/discovery_form.html', {'form': form})


def delete_discovery(request, pk):
    discover = get_object_or_404(Discover, pk=pk)
    if request.method == 'POST':
        discover.delete()
    return redirect('discovery-list')
