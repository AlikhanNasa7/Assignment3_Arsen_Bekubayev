from django.urls import path
from . import views

urlpatterns = [
    path('', views.disease_list, name='disease-list'),
    path('create/', views.create_disease, name='disease-create'),
    path('update/<str:pk>/', views.update_disease, name='disease-update'),
    path('delete/<str:pk>/', views.delete_disease, name='disease-delete'),
]