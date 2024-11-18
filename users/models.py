from django.db import models
from countries.models import Country


class Users(models.Model):
    email = models.CharField(primary_key=True, max_length=60)
    name = models.CharField(max_length=30, blank=True, null=True)
    surname = models.CharField(max_length=40, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    cname = models.ForeignKey(Country, models.CASCADE, db_column='cname', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Users'

    def __str__(self):
        return self.email
