from django.db import models


class Publicservant(models.Model):
    email = models.OneToOneField('users.Users', models.CASCADE, db_column='email', primary_key=True)
    department = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PublicServant'


    def __str__(self):
        return self.email.email