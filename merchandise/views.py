from django.shortcuts import render
from .models import Merchandise


# Create your views here.

def all_products(request):
    products = Merchandise.objects.all()
    return render(request, 'merchandise\merchandise.html', {"products": products})
