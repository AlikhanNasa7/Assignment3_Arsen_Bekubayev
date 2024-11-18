from django import forms
from countries.models import Country
from discoveries.models import Discover
from diseases.models import Disease
from diseases_types.models import Diseasetype
from doctors.models import Doctor
from patient_diseases.models import Patientdisease
from patients.models import Patients
from public_servants.models import Publicservant
from records.models import Record
from specializes.models import Specialize
from users.models import Users


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['cname', 'population']


class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = ['disease_code', 'pathogen', 'description', 'disease_type']
        labels = {
            'disease_code': 'Disease Code',
            'pathogen': 'Pathogen',
            'description': 'Description',
            'disease_type': 'Disease Type (ID)',
        }


class DiscoverForm(forms.ModelForm):
    class Meta:
        model = Discover
        fields = ['cname', 'disease_code', 'first_enc_date']
        widgets = {
            'first_enc_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'cname': 'Country Name',
            'disease_code': 'Disease Code',
            'first_enc_date': 'First Encounter Date',
        }


class DiseaseTypeForm(forms.ModelForm):
    class Meta:
        model = Diseasetype
        fields = ['id', 'description']
        labels = {
            'id': 'ID',
            'description': 'Description',
        }


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['email', 'degree']
        labels = {
            'email': 'Email',
            'degree': 'Degree',
        }


class PatientDiseaseForm(forms.ModelForm):
    class Meta:
        model = Patientdisease
        fields = ['email', 'disease_code']
        labels = {
            'email': 'Patient Email',
            'disease_code': 'Disease Code',
        }


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = ['email']
        labels = {
            'email': 'Email',
        }


class PublicServantForm(forms.ModelForm):
    class Meta:
        model = Publicservant
        fields = ['email', 'department']
        labels = {
            'email': 'Email',
            'department': 'Department',
        }


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['email', 'cname', 'disease_code', 'total_deaths', 'total_patients']
        labels = {
            'email': 'Public Servant Email',
            'cname': 'Country Name',
            'disease_code': 'Disease Code',
            'total_deaths': 'Total Deaths',
            'total_patients': 'Total Patients',
        }


class SpecializeForm(forms.ModelForm):
    class Meta:
        model = Specialize
        fields = ['diseasetype', 'doctor']
        labels = {
            'diseasetype': 'Disease Type (ID)',
            'doctor': 'Doctor Email',
        }


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'
        labels = {
            'id': 'Disease Type (ID)',
            'email': 'Doctor Email',
        }
