from django import forms
from .models import Bikes
# from .views import manufacturer_list, cylinders_list, layout_list


#  set in global scope so can be used by all list functions
bike_list = Bikes.objects.all()


#  create a list of tuples of unique manufacturers for the drop-down menu
def manufacturer_list():

    a = set(bike.manufacturer for bike in bike_list)
    b = ['All'] + list(a)
    c = [(x, x) for x in b]
    return c


#  create a list of tuples of unique number of cylinders for the drop-down menu
def cylinders_list():

    a = set(bike.cylinders for bike in bike_list)
    b = ['All'] + list(a)
    c = [(x, x) for x in b]

    return c


#  create a list of tuples of unique engine layouts for the drop-down menu
def layout_list():

    a = set(bike.layout for bike in bike_list)
    b = ['All'] + list(a)
    c = [(x, x) for x in b]

    return c


class BikeSearchForm(forms.Form):

    manufacturer = forms.ChoiceField(choices=manufacturer_list, initial='All')
    cylinders = forms.ChoiceField(choices=cylinders_list, initial='All')
    layout = forms.ChoiceField(choices=layout_list, initial='All')

    class Meta:
        # model = Bikes
        fields = ('manufacturer', 'cylinders', 'layout')
