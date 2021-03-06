from django.shortcuts import render
from .models import Bike, Manufacturer
from .forms import BikeSearchForm


def bike_search(request):
    """
    Return a list of bikes which match the chosen criteria
    """
    # form process:
    if 'action' in request.GET and request.GET['action'] == 'process_form':
        form = BikeSearchForm(request.GET)

        cursor = Bike.objects.all()
        selected_manufacturer = request.GET.get('manufacturer', '')
        selected_cylinders = request.GET.get('cylinders', '')
        selected_layout = request.GET.get('layout', '')

        if selected_manufacturer != 'All':
            manufacturer = Manufacturer.objects.get(name=selected_manufacturer)
            cursor = cursor.filter(manufacturer=manufacturer)
            form.initial['manufacturer'] = manufacturer

        if selected_cylinders != 'All':
            cursor = cursor.filter(cylinders=selected_cylinders)

        if selected_layout != 'All':
            cursor = cursor.filter(layout__layout=selected_layout)

        bikes = list(cursor.order_by('manufacturer'))

    # form display:
    else:
        form = BikeSearchForm()
        bikes = []
    args = {'form': form, 'bikes': bikes}

    return render(request, 'bike_selector/bike_selector.html', args)
