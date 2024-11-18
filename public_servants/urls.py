from django.urls import path
from . import views

urlpatterns = [
    path('', views.servant_list, name='servant-list'),
    path('create/', views.create_servant, name='servant-create'),
    path('update/<str:pk>/', views.update_servant, name='servant-update'),
    path('delete/<str:pk>/', views.delete_servant, name='servant-delete'),
]