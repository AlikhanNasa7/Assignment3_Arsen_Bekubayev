from django.db import models
from diseases.models import Disease


class Patientdisease(models.Model):
    email = models.ForeignKey('users.Users', models.CASCADE, db_column='email', blank=True, null=True)
    disease_code = models.ForeignKey(Disease, models.CASCADE, db_column='disease_code', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PatientDisease'


    def __str__(self):
        return f"{self.email} - {self.disease_code}"