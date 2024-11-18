from django.db import models
from public_servants.models import Publicservant
from countries.models import Country
from diseases.models import Disease


class Record(models.Model):
    email = models.ForeignKey(Publicservant, models.CASCADE, db_column='email', blank=True, null=True)
    cname = models.ForeignKey(Country, models.CASCADE, db_column='cname', blank=True, null=True)
    disease_code = models.ForeignKey(Disease, models.CASCADE, db_column='disease_code', blank=True, null=True)
    total_deaths = models.IntegerField(blank=True, null=True)
    total_patients = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Record'

    def __str__(self):
        return str(self.email)
