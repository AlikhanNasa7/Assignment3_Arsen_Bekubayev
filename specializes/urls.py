from django.urls import path
from . import views

urlpatterns = [
    path('', views.specialize_list, name='specialize-list'),
    path('create/', views.create_specialize, name='specialize-create'),
    path('update/<str:pk>/', views.update_specialize, name='specialize-update'),
    path('delete/<str:pk>/', views.delete_specialize, name='specialize-delete'),
]