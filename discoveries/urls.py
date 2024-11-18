from django.urls import path
from . import views

urlpatterns = [
    path('', views.discovery_list, name='discovery-list'),
    path('create/', views.create_discovery, name='discovery-create'),
    path('update/<str:pk>/', views.update_discovery, name='discovery-update'),
    path('delete/<str:pk>/', views.delete_discovery, name='discovery-delete'),
]