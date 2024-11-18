from django.db import models
from countries.models import Country


class Discover(models.Model):
    cname = models.ForeignKey(Country, models.DO_NOTHING, db_column='cname', blank=True, null=True)
    disease_code = models.OneToOneField('diseases.Disease', models.CASCADE, db_column='disease_code', primary_key=True)
    first_enc_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Discover'

    def __str__(self):
        return self.disease_code
