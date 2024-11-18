from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor_list, name='doctor-list'),
    path('create/', views.create_doctor, name='doctor-create'),
    path('update/<str:pk>/', views.update_doctor, name='doctor-update'),
    path('delete/<str:pk>/', views.delete_doctor, name='doctor-delete'),
]