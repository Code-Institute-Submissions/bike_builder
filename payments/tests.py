from django.test import TestCase
from views import place_order
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response


class PaymentsPageTest(TestCase):

    # URL test
    # Place_order also requires an arg (product_id)
    def test_payments_page_resolves(self):
        get_place_order_page = resolve('/place_order/<product_id>/')
        self.assertEqual(get_place_order_page.func, place_order)

    # Status code test
    def test_payments_page_status_code_is_okay(self):
        payments_page = self.client.get('/place_order/<product_id>/')
        self.assertEqual(payments_page.status_code, 200)

    # Content test
    def test_payments_page_check_content_is_correct(self):
        payments_page = self.client.get('/place_order/<product_id>/')
        self.assertTemplateUsed(payments_page, "payments/make_payment.html")
        payments_page_template_output = render_to_response("payments/make_payment.html").content
        self.assertEqual(payments_page.content, payments_page_template_output)
