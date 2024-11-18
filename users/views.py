from django.shortcuts import render, redirect, get_object_or_404
from .models import Users
from health_forms.forms import UsersForm


def user_list(request):
    users = Users.objects.all()
    return render(request, 'users/index.html', {'users': users, 'heading': 'Users'})


def create_user(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-list')
    else:
        form = UsersForm()
    return render(request, 'users/users_form.html', {'form': form, 'heading': 'Create User'})


def update_user(request, pk):
    user = Users.objects.get(pk=pk)
    if request.method == 'POST':
        form = UsersForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-list')
    else:
        form = UsersForm(instance=user)
    return render(request, 'users/users_form.html', {'form': form, 'heading': 'Update User'})


def delete_user(request, pk):
    user = Users.objects.get(pk=pk)
    if request.method == 'POST':
        user.delete()
    return redirect('user-list')