# Generated by Django 2.1.5 on 2019-01-27 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20190127_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='accident',
            name='CD_GENRE_ACCDN',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='GRAVITE',
            field=models.CharField(default='Not specified', max_length=30),
        ),
        migrations.AddField(
            model_name='accident',
            name='HEURE_ACCDN',
            field=models.CharField(default='Not specified', max_length=30),
        ),
        migrations.AddField(
            model_name='accident',
            name='LOC_LAT',
            field=models.DecimalField(decimal_places=7, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='accident',
            name='LOC_LONG',
            field=models.DecimalField(decimal_places=7, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='accident',
            name='NB_BLESSES_LEGERS',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='NB_BLESSES_MOTO',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='NB_BLESSES_PIETON',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='NB_BLESSES_Sevre',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='NB_BLESSES_VELO',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='NB_DECES_MOTO',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='NB_DECES_PIETON',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='NB_DECES_VELO',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='NB_MORTS',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='NB_VEH_IMPLIQUES_ACCDN',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='NB_VICTIMES_MOTO',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='NB_VICTIMES_PIETON',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='NB_VICTIMES_TOTAL',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='NB_VICTIMES_VELO',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='RUE_ACCDN',
            field=models.CharField(default='Not specified', max_length=30),
        ),
        migrations.AddField(
            model_name='accident',
            name='nb_VHR',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='nb_automobile_camion_leger',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='nb_autres_types',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='nb_bicyclette',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='nb_camionLourd_tractRoutier',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='nb_cyclomoteur',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='nb_motocyclette',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='nb_motoneige',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='nb_outil_equipement',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='nb_taxi',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='nb_tous_autobus_minibus',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='nb_urgence',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accident',
            name='nb_veh_non_precise',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='accident',
            name='DT_ACCDN',
            field=models.CharField(default='Not specified', max_length=30),
        ),
        migrations.AlterField(
            model_name='accident',
            name='NO_CIVIQ_ACCDN',
            field=models.IntegerField(default=0),
        ),
    ]