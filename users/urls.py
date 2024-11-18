from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user-list'),
    path('create/', views.create_user, name='user-create'),
    path('update/<str:pk>/', views.update_user, name='user-update'),
    path('delete/<str:pk>/', views.delete_user, name='user-delete'),
]