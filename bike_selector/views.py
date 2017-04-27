from django.shortcuts import render
from django.http import HttpResponse
from .models import Bikes
from .forms import BikeSearchForm


# # Create your views here.
# def bike_selector(request):
#     return render(request, 'bike_selector/bike_selector.html')


# #  set in global scope so can be used by all list functions
# bike_list = Bikes.objects.all()
#
#
# #  create a list of tuples of unique manufacturers for the drop-down menu
# def manufacturer_list(request):
#
#     a = set(bike.manufacturer for bike in bike_list)
#     b = ['All'] + list(a)
#     c = [(x, x) for x in b]
#     return c
#
#
# #  create a list of tuples of unique number of cylinders for the drop-down menu
# def cylinders_list(request):
#
#     a = set(bike.cylinders for bike in bike_list)
#     b = ['All'] + list(a)
#     c = [(x, x) for x in b]
#
#     return c
#
#
# #  create a list of tuples of unique engine layouts for the drop-down menu
# def layout_list(request):
#
#     a = set(bike.layout for bike in bike_list)
#     b = ['All'] + list(a)
#     c = [(x, x) for x in b]
#
#     return c


#  search for the bikes which match the chosen criteria
def bike_search(request):

    if request.method == 'POST':
        form = BikeSearchForm(request.GET)

        cursor = Bikes.objects.all()
        selected_manufacturer = request.GET['manufacturer']
        selected_cylinders = request.GET['cylinders']
        selected_layout = request.GET['layout']

        if selected_manufacturer != 'All':
            cursor = cursor.filter(manufacturer=selected_manufacturer)

        if selected_cylinders != 'All':
            cursor = cursor.filter(cylinders=selected_cylinders)

        if selected_layout != 'All':
            cursor = cursor.filter(layout=selected_layout)

        cursor = cursor.order_by('manufacturer')

        return list(cursor)

    else:
        form = BikeSearchForm()

    args = {'form': form}

    return render(request, 'bike_selector/bike_selector.html', args)
