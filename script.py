# [Must run this script inside django shell]
# This script for responsible for populating the local db with the data from the csv file
# called 'Accidents_2012_2017.csv' located in the root directory. This script only needs to
# be called once.

import csv

from boards.models import Accident # imports the model
with open('Accidents_2012_2017.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = Accident(DT_ACCDN=row['DT_ACCDN'], NO_CIVIQ_ACCDN=row['NO_CIVIQ_ACCDN'], RUE_ACCDN=row['RUE_ACCDN'], CD_GENRE_ACCDN=row['CD_GENRE_ACCDN'], NB_VEH_IMPLIQUES_ACCDN=row['NB_VEH_IMPLIQUES_ACCDN'], NB_MORTS=row['NB_MORTS'], NB_BLESSES_Sevre=row['NB_BLESSES_Sevre'], NB_BLESSES_LEGERS=row['NB_BLESSES_LEGERS'], HEURE_ACCDN=row['HEURE_ACCDN'], NB_VICTIMES_TOTAL=row['NB_VICTIMES_TOTAL'], GRAVITE=row['GRAVITE'], nb_automobile_camion_leger=row['nb_automobile_camion_leger'], nb_camionLourd_tractRoutier=row['nb_camionLourd_tractRoutier'], nb_outil_equipement=row['nb_outil_equipement'], nb_tous_autobus_minibus=row['nb_tous_autobus_minibus'], nb_bicyclette=row['nb_bicyclette'], nb_cyclomoteur=row['nb_cyclomoteur'], nb_motocyclette=row['nb_motocyclette'], nb_taxi=row['nb_taxi'], nb_urgence=row['nb_urgence'], nb_motoneige=row['nb_motoneige'], nb_VHR=row['nb_VHR'], nb_autres_types=row['nb_autres_types'], nb_veh_non_precise=row['nb_veh_non_precise'], NB_DECES_PIETON=row['NB_DECES_PIETON'], NB_BLESSES_PIETON=row['NB_BLESSES_PIETON'], NB_VICTIMES_PIETON=row['NB_VICTIMES_PIETON'], NB_DECES_MOTO=row['NB_DECES_MOTO'], NB_BLESSES_MOTO=row['NB_BLESSES_MOTO'], NB_VICTIMES_MOTO=row['NB_VICTIMES_MOTO'], NB_DECES_VELO=row['NB_DECES_VELO'], NB_BLESSES_VELO=row['NB_BLESSES_VELO'], NB_VICTIMES_VELO=row['NB_VICTIMES_VELO'], LOC_LONG=row['LOC_LONG'], LOC_LAT=row['LOC_LAT'])
        p.save()


exit()