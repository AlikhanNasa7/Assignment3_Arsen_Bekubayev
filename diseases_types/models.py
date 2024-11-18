from django.db import models


class Diseasetype(models.Model):
    description = models.CharField(max_length=140, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DiseaseType'

    def __str__(self):
        return str(self.id)