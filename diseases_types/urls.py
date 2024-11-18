from django.urls import path
from . import views

urlpatterns = [
    path('', views.diseasetype_list, name='diseasetype-list'),
    path('create/', views.create_diseasetype, name='diseasetype-create'),
    path('update/<str:pk>/', views.update_diseasetype, name='diseasetype-update'),
    path('delete/<str:pk>/', views.delete_diseasetype, name='diseasetype-delete'),
]