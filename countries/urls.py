from django.urls import path
from . import views

urlpatterns = [
    path('', views.country_list, name='country-list'),
    path('create/', views.create_country, name='country-create'),
    path('update/<str:pk>/', views.update_country, name='country-update'),
    path('delete/<str:pk>/', views.delete_country, name='country-delete'),
]