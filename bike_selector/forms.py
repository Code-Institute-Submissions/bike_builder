from django import forms
from .models import Bike


#  set in global scope so can be used by all list functions
bike_list = Bike.objects.all().order_by('manufacturer')


def manufacturer_list():
    """
    Create a list of tuples of unique manufacturers 
    for the drop-down menu
    """
    a = set(bike.manufacturer for bike in bike_list)
    b = ['All'] + sorted(list(a))
    c = [(x, x) for x in b]
    return sorted(c)


def cylinders_list():
    """
    Create a list of tuples of unique number of 
    cylinders for the drop-down menu
    """
    a = set(bike.cylinders for bike in bike_list)
    b = ['All'] + list(a)
    c = [(x, x) for x in b]
    return c


def layout_list():
    """
    Create a list of tuples of unique engine 
    layouts for the drop-down menu
    """
    a = set(bike.layout for bike in bike_list)
    b = ['All'] + list(a)
    c = [(x, x) for x in b]
    return c


class BikeSearchForm(forms.Form):
    """
    Form with dropdown menus from which user
    selects criteria
    """
    manufacturer = forms.ChoiceField(choices=manufacturer_list, initial='All')
    cylinders = forms.ChoiceField(choices=cylinders_list, initial='All')
    layout = forms.ChoiceField(choices=layout_list, initial='All')

    class Meta:
        fields = ("name", 'cylinders', 'layout')
