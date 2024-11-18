from django.db import models


class Disease(models.Model):
    disease_code = models.CharField(primary_key=True, max_length=50)
    pathogen = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=140, blank=True, null=True)
    disease_type = models.ForeignKey(
        'diseases_types.Diseasetype',
        on_delete=models.CASCADE,
        db_column='id'
    )

    class Meta:
        managed = False
        db_table = 'Disease'

    def __str__(self):
        return self.disease_code

