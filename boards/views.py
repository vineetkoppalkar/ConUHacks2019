from django.shortcuts import render
from boards.models import Accident

def home(request):

    # Used to clear all objects in db
    # Accident.objects.all().delete()

    allAccidents = Accident.objects.all()
    allLocations = []

    for accident in allAccidents:
        location = []
        location.append(float(accident.LOC_LONG))
        location.append(float(accident.LOC_LAT))
        allLocations.append(location)

    context = {'allLocations': allLocations}

    return render(request, "index.html", context)
