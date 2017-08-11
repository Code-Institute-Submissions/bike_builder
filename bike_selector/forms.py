from django import forms
from .models import Bike


#  set in global scope so can be used by all list functions
bike_list = Bike.objects.all().order_by('manufacturer')


def manufacturer_list():
    """
    Create a list of tuples of unique manufacturers 
    for the drop-down menu
    """
    man_list = []
    for bike in bike_list:
        if bike.manufacturer not in man_list:
            man_list.append(bike.manufacturer)
    man_tuples = [(manufacturer, manufacturer) for manufacturer in man_list]  # create a list of tuples
    complete_man_tuples = [('All', 'All')] + man_tuples  # add 'All' here so it appears at top of list
    return complete_man_tuples


def cylinders_list():
    """
    Create a list of tuples of unique number of 
    cylinders for the drop-down menu
    """
    cyl_list = list(set(bike.cylinders for bike in bike_list))
    cyl_tuples = [(cylinders, cylinders) for cylinders in cyl_list]
    cyl_tuples.sort()
    complete_cyl_tuples = [('All', 'All')] + cyl_tuples
    return complete_cyl_tuples


def layout_list():
    """
    Create a list of tuples of unique engine 
    layouts for the drop-down menu
    """
    lay_list = list(set(bike.layout for bike in bike_list))
    lay_tuples = [(layout, layout) for layout in lay_list]
    lay_tuples.sort()
    complete_lay_tuples = [('All', 'All')] + lay_tuples
    return complete_lay_tuples


class BikeSearchForm(forms.Form):
    """
    Form with dropdown menus from which user
    selects criteria
    """
    manufacturer = forms.ChoiceField(choices=manufacturer_list, initial='All')
    cylinders = forms.ChoiceField(choices=cylinders_list, initial='All')
    layout = forms.ChoiceField(choices=layout_list, initial='All')

    class Meta:
        fields = ('name', 'cylinders', 'layout')

# from django import forms
# from .models import Bike
#
#
# #  set in global scope so can be used by all list functions
# bike_list = Bike.objects.all().order_by('manufacturer')
#
#
# def manufacturer_list():
#     """
#     Create a list of tuples of unique manufacturers
#     for the drop-down menu
#     """
#     a = set(bike.manufacturer for bike in bike_list)
#     b = ['All'] + (list(a))
#     c = sorted([(x, x) for x in b])
#     return c
#
#
# def cylinders_list():
#     """
#     Create a list of tuples of unique number of
#     cylinders for the drop-down menu
#     """
#     a = set(bike.cylinders for bike in bike_list)
#     b = ['All'] + list(a)
#     c = [(x, x) for x in b]
#     return c
#
#
# def layout_list():
#     """
#     Create a list of tuples of unique engine
#     layouts for the drop-down menu
#     """
#     a = set(bike.layout for bike in bike_list)
#     b = ['All'] + list(a)
#     c = [(x, x) for x in b]
#     return c
#
#
# class BikeSearchForm(forms.Form):
#     """
#     Form with dropdown menus from which user
#     selects criteria
#     """
#     manufacturer = forms.ChoiceField(choices=manufacturer_list, initial='All')
#     cylinders = forms.ChoiceField(choices=cylinders_list, initial='All')
#     layout = forms.ChoiceField(choices=layout_list, initial='All')
#
#     class Meta:
#         fields = ("name", 'cylinders', 'layout')
#
