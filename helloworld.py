from __future__ import unicode_literals

from django.db import models


class Adresse(models.Model):
    adresseid = models.AutoField(db_column='AdresseId', primary_key=True)  # Field name made lowercase.
    villeid = models.ForeignKey('Ville', db_column='VilleId', blank=True, null=True)  # Field name made lowercase.
    adresse1 = models.CharField(db_column='Adresse1', max_length=50)  # Field name made lowercase.
    adresse2 = models.CharField(db_column='Adresse2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    valide = models.IntegerField(db_column='Valide')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Adresse'
