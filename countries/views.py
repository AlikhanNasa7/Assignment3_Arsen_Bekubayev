from django.shortcuts import render, redirect, get_object_or_404
from .models import Country
from health_forms.forms import CountryForm


def country_list(request):
    countries = Country.objects.all()
    return render(request, 'countries/index.html', {'countries': countries, 'heading': 'Countries'})


def create_country(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('country-list')
    else:
        form = CountryForm()
    return render(request, 'countries/country_form.html', {'form': form, 'heading': 'Create Country'})


def update_country(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == 'POST':
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            form.save()
            return redirect('country-list')
    else:
        form = CountryForm(instance=country)
    return render(request, 'countries/country_form.html', {'form': form})


def delete_country(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == 'POST':
        country.delete()
    return redirect('country-list')
