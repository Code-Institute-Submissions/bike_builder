from django import forms
from .models import Purchase


class PaymentForm(forms.ModelForm):

    MONTH_ABBREVIATIONS = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ]
    MONTH_CHOICES = list(enumerate(MONTH_ABBREVIATIONS, 1))
    YEAR_CHOICES = [(i, i) for i in xrange(2017, 2038)]

    # item = forms.IntegerField(label='Item')
    credit_card_number = forms.CharField(label='Credit card number')
    cvv = forms.CharField(label='Security code (CVV)')
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = Purchase
        # fields = ('item',
        fields = ('first_name',
                  'last_name',
                  'address_line_1',
                  'address_line_2',
                  'address_line_3',
                  'address_line_4',
                  'post_code',
                  'email_address',
                  'credit_card_number',
                  'cvv',
                  'expiry_month',
                  'expiry_year',
                  'stripe_id',
                  )
