from django.shortcuts import render
from .models import Merchandise


def all_products(request):
    """
    Show all merchandise items
    """
    products = Merchandise.objects.all().order_by('price')
    return render(request, 'merchandise/merchandise.html', {"products": products})
