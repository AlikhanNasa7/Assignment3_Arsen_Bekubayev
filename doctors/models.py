from django.db import models


class Doctor(models.Model):
    email = models.OneToOneField('users.Users', models.CASCADE, db_column='email', primary_key=True)
    degree = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Doctor'

    def __str__(self):
        return self.email.email
