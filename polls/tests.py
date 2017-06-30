from django.test import TestCase
from views import place_order
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response


# URL test
# Place_order also has an arg (product_id): does this need to be included in the url?
class PaymentsPageTest(TestCase):
    def test_payments_page_resolves(self):
        get_place_order_page = resolve('/place_order/')
        self.assertEqual(get_place_order_page.func, place_order)
