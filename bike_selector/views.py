from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def bike_selector(request):
    return render(request, 'bike_selector/bike_selector.html')
