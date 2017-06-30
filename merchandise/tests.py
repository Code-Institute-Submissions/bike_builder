from django.test import TestCase
from views import all_products
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response


class MerchandisePageTest(TestCase):

    # URL test
    def test_merchandise_page_resolves(self):
        get_merchandise_page = resolve('/merchandise/')
        self.assertEqual(get_merchandise_page.func, all_products)

    # Status code test
    def test_merchandise_page_status_code_is_okay(self):
        merchandise_page = self.client.get('/merchandise/')
        self.assertEqual(merchandise_page.status_code, 200)

    # Content test
    def test_gallery_page_check_content_is_correct(self):
        merchandise_page = self.client.get('/merchandise/')
        self.assertTemplateUsed(merchandise_page, "merchandise/merchandise.html")
        merchandise_page_template_output = render_to_response("merchandise/merchandise.html").content
        self.assertEqual(merchandise_page.content, merchandise_page_template_output)
