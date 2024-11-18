from django.urls import path
from . import views

urlpatterns = [
    path('', views.patientdisease_list, name='patientdisease-list'),
    path('create/', views.create_patientdisease, name='patientdisease-create'),
    path('update/<str:pk>/', views.update_patientdisease, name='patientdisease-update'),
    path('delete/<str:pk>/', views.delete_patientdisease, name='patientdisease-delete'),
]