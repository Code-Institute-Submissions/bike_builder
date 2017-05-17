from django import forms
from .models import HowTo


class HowToForm(forms.ModelForm):

    class Meta:
        model = HowTo
        fields = ['description', 'url']

    url = forms.URLField(label='url', initial='http://')
