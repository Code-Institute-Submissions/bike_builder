from django.test import TestCase
from views import place_order
from forms import PaymentForm
from django.core.urlresolvers import resolve
from django import forms


class PaymentsPageTest(TestCase):

    def test_payments_page_resolves(self):
        place_order_page = resolve('/place_order/1/')
        self.assertEqual(place_order_page.func, place_order)

    def test_payments_form_with_missing_last_name(self):
        form = PaymentForm({
            'first_name': 'eric',
            'address_line_1': '28201 E. Bonanza St.',
            'address_line_2': 'South Park',
            'address_line_3': '',
            'address_line_4': '',
            'post_code': 'er1 1ic',
            'email_address': 'eric.cartman@gmail.com',
            'credit_card_number': '4242424242424242',
            'cvv': '123',
            'expiry_month': 'Jan',
            'expiry_year': '2037',
            'stripe_id': 'test_stripe_id'
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please fill in this field",
                                 form.full_clean())
