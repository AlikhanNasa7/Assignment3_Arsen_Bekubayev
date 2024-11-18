from django.db import models


class Patients(models.Model):
    email = models.OneToOneField('users.Users', models.CASCADE, db_column='email', primary_key=True)

    class Meta:
        managed = False
        db_table = 'Patients'

    def __str__(self):
        return self.email