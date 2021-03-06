from django.db import models

# Create your models here.
class Accident(models.Model):
    DT_ACCDN = models.CharField(max_length=30, default='Not specified')
    NO_CIVIQ_ACCDN = models.CharField(max_length=30, default='Not specified')
    RUE_ACCDN = models.CharField(max_length=30, default='Not specified')
    CD_GENRE_ACCDN = models.CharField(max_length=30, default='Not specified')
    NB_VEH_IMPLIQUES_ACCDN = models.CharField(max_length=30, default='Not specified')
    NB_MORTS = models.CharField(max_length=30, default='Not specified')
    NB_BLESSES_Sevre = models.CharField(max_length=30, default='Not specified')
    NB_BLESSES_LEGERS = models.CharField(max_length=30, default='Not specified')
    HEURE_ACCDN = models.CharField(max_length=30, default='Not specified')
    NB_VICTIMES_TOTAL = models.CharField(max_length=30, default='Not specified')
    GRAVITE = models.CharField(max_length=30, default='Not specified')
    nb_automobile_camion_leger = models.CharField(max_length=30, default='Not specified')
    nb_camionLourd_tractRoutier = models.CharField(max_length=30, default='Not specified')
    nb_outil_equipement = models.CharField(max_length=30, default='Not specified')
    nb_tous_autobus_minibus = models.CharField(max_length=30, default='Not specified')
    nb_bicyclette = models.CharField(max_length=30, default='Not specified')
    nb_cyclomoteur = models.CharField(max_length=30, default='Not specified')
    nb_motocyclette = models.CharField(max_length=30, default='Not specified')
    nb_taxi = models.CharField(max_length=30, default='Not specified')
    nb_urgence = models.CharField(max_length=30, default='Not specified')
    nb_motoneige = models.CharField(max_length=30, default='Not specified')
    nb_VHR = models.CharField(max_length=30, default='Not specified')
    nb_autres_types = models.CharField(max_length=30, default='Not specified')
    nb_veh_non_precise = models.CharField(max_length=30, default='Not specified')
    NB_DECES_PIETON = models.CharField(max_length=30, default='Not specified')
    NB_BLESSES_PIETON = models.CharField(max_length=30, default='Not specified')
    NB_VICTIMES_PIETON = models.CharField(max_length=30, default='Not specified')
    NB_DECES_MOTO = models.CharField(max_length=30, default='Not specified')
    NB_BLESSES_MOTO = models.CharField(max_length=30, default='Not specified')
    NB_VICTIMES_MOTO = models.CharField(max_length=30, default='Not specified')
    NB_DECES_VELO = models.CharField(max_length=30, default='Not specified')
    NB_BLESSES_VELO = models.CharField(max_length=30, default='Not specified')
    NB_VICTIMES_VELO = models.CharField(max_length=30, default='Not specified')
    LOC_LONG = models.DecimalField(max_digits=10, decimal_places=7, default=0)
    LOC_LAT = models.DecimalField(max_digits=10, decimal_places=7, default=0)
