from django.test import TestCase
from views import home_page
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response


class HomePageTest(TestCase):

    # URL test
    def test_home_page_resolves(self):
        get_home_page = resolve('/')
        self.assertEqual(get_home_page.func, home_page)

    # Status code test
    def test_home_page_status_code_is_okay(self):
        get_home_page = self.client.get('/')
        self.assertEqual(get_home_page.status_code, 200)

    # Content test
    def test_check_content_is_correct(self):
        get_home_page = self.client.get('/')
        self.assertTemplateUsed(get_home_page, "home/home.html")
        home_page_template_output = render_to_response("home/home.html").content
        self.assertEqual(get_home_page.content, home_page_template_output)
