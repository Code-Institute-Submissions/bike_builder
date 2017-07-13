from django.test import TestCase
from views import how_to_guides, upload_guide
from django.core.urlresolvers import resolve
from forms import HowToForm
from django import forms
from django.shortcuts import render_to_response


class HowToGuidesPageTest(TestCase):

    def test_how_to_guides_page_resolves(self):
        how_to_guides_page = resolve('/how_to_guides/')
        self.assertEqual(how_to_guides_page.func, how_to_guides)

    def test_how_to_guides_page_status_code_is_okay(self):
        how_to_guides_page = self.client.get('/how_to_guides/')
        self.assertEqual(how_to_guides_page.status_code, 200)

    def test_check_how_to_guides_page_content_is_correct(self):
        how_to_guides_page = self.client.get('/how_to_guides/')
        self.assertTemplateUsed(how_to_guides_page, "how_to_guides/how_to_guides.html")
        how_to_guides_page_template_output = render_to_response("how_to_guides/how_to_guides.html").content
        self.assertEqual(how_to_guides_page.content, how_to_guides_page_template_output)

    def test_upload_guides_page_resolves(self):
        upload_guides_page = resolve('/how_to_guides/upload_guide/')
        self.assertEqual(upload_guides_page.func, upload_guide)

    def test_upload_guides_page_status_code_is_okay(self):
        upload_guides_page = self.client.get('/how_to_guides/')
        self.assertEqual(upload_guides_page.status_code, 200)

    def test_upload_guides_form_success(self):
        form = HowToForm({
            'description': 'test description of how-to guide',
            'url': 'https://www.test.com'
        })
        self.assertTrue(form.is_valid())

    def test_upload_guides_form_with_missing_link(self):
        form = HowToForm({
            'description': 'test description of how-to guide'
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter a URL",
                                 form.full_clean())
