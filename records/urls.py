from django.urls import path
from . import views

urlpatterns = [
    path('', views.record_list, name='record-list'),
    path('create/', views.create_record, name='record-create'),
    path('update/<str:pk>/', views.update_record, name='record-update'),
    path('delete/<str:pk>/', views.delete_record, name='record-delete'),
]