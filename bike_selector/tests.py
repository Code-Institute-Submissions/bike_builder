from django.test import TestCase
from views import bike_search
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response


class BikeSelectorPageTest(TestCase):

    # URL test
    def test_bike_selector_page_resolves(self):
        get_bike_selector_page = resolve('/bike_selector/')
        self.assertEqual(get_bike_selector_page.func, bike_search)

    # Status code test
    def test_bike_selector_page_status_code_is_okay(self):
        bike_selector_page = self.client.get('/bike_selector/')
        self.assertEqual(bike_selector_page.status_code, 200)

    # Content test
    def test_bike_selector_page_check_content_is_correct(self):
        bike_selector_page = self.client.get('/bike_selector/')
        self.assertTemplateUsed(bike_selector_page, "bike_selector/bike_selector.html")
        bike_selector_page_template_output = render_to_response("bike_selector/bike_selector.html").content
        self.assertEqual(bike_selector_page.content, bike_selector_page_template_output)
