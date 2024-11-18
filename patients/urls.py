from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient_list, name='patient-list'),
    path('create/', views.create_patient, name='patient-create'),
    path('update/<str:pk>/', views.update_patient, name='patient-update'),
    path('delete/<str:pk>/', views.delete_patient, name='patient-delete'),
]