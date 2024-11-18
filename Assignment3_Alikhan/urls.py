from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('countries/', include('countries.urls'), name='countries'),
    path('discoveries/', include('discoveries.urls'), name='discoveries'),
    path('diseases/', include('diseases.urls'), name='diseases'),
    path('diseases_types/', include('diseases_types.urls'), name='diseases_types'),
    path('doctors/', include('doctors.urls'), name='doctors'),
    path('patient_diseases/', include('patient_diseases.urls'), name='patient_diseases'),
    path('patients/', include('patients.urls'), name='patients'),
    path('public_servants/', include('public_servants.urls'), name='public_servants'),
    path('records/', include('records.urls'), name='records'),
    path('specializes/', include('specializes.urls'), name='specializes'),
    path('users/', include('users.urls'), name='users'),
]
