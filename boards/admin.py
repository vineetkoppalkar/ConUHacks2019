from django.contrib import admin
from boards.models import Accident

class AccidentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'DT_ACCDN',
        'NO_CIVIQ_ACCDN',
        'RUE_ACCDN',
        'CD_GENRE_ACCDN',
        'NB_VEH_IMPLIQUES_ACCDN',
        'NB_MORTS',
        'NB_BLESSES_Sevre',
        'NB_BLESSES_LEGERS',
        'HEURE_ACCDN',
        'NB_VICTIMES_TOTAL',
        'GRAVITE',
        'LOC_LONG',
        'LOC_LAT'
    )
    list_display_links = ('id', 'DT_ACCDN')
    search_fields = ('DT_ACCDN', 'content')
    list_per_page = 25

admin.site.register(Accident, AccidentAdmin)
