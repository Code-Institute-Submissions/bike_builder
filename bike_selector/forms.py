from django import forms
from .models import Bikes
from .views import manufacturer_list, cylinders_list, layout_list


class BikeSearchForm(forms.ModelForm):

    manufacturer = forms.ChoiceField(choices=manufacturer_list)
    cylinders = forms.ChoiceField(choices=cylinders_list)
    layout = forms.ChoiceField(choices=layout_list)

    class Meta:
        model = Bikes
        fields = ('manufacturer', 'cylinders', 'layout')
