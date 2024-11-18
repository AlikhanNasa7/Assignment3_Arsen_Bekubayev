from django.db import models
from diseases_types.models import Diseasetype
from doctors.models import Doctor


class Specialize(models.Model):
    diseasetype = models.OneToOneField(
        Diseasetype,
        models.CASCADE,
        db_column='id',
        primary_key=True,
        related_name='specialization'
    )
    doctor = models.ForeignKey(
        Doctor,
        models.CASCADE,
        db_column='email',
        related_name='specializations'
    )

    class Meta:
        managed = False
        db_table = 'Specialize'
        unique_together = (('diseasetype', 'doctor'),)

    def __str__(self):
        return f"{self.diseasetype.description} - {self.doctor.email}"
