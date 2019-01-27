from django.shortcuts import render
from boards.models import Accident

def home(request):
    return render(request, "index.html")
