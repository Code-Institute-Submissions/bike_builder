from django.test import TestCase
from views import gallery, upload_image
from forms import GalleryForm
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from django import forms


class GalleryPageTest(TestCase):

    # Gallery
    # URL test
    def test_gallery_page_resolves(self):
        get_gallery_page = resolve('/gallery/')
        self.assertEqual(get_gallery_page.func, gallery)

    # Status code test
    def test_gallery_page_status_code_is_okay(self):
        gallery_page = self.client.get('/gallery/')
        self.assertEqual(gallery_page.status_code, 200)

    # Content test
    def test_gallery_page_check_content_is_correct(self):
        gallery_page = self.client.get('/gallery/')
        self.assertTemplateUsed(gallery_page, "gallery/gallery.html")
        gallery_page_template_output = render_to_response("gallery/gallery.html").content
        self.assertEqual(gallery_page.content, gallery_page_template_output)

    # Gallery upload
    # URL test
    def test_gallery_upload_page_resolves(self):
        get_gallery_form_page = resolve('/gallery/upload_image/')
        self.assertEqual(get_gallery_form_page.func, upload_image)

    # Status code test
    def test_gallery_upload_page_status_code_is_okay(self):
        gallery_upload_page = self.client.get('/gallery/upload_image/')
        self.assertEqual(gallery_upload_page.status_code, 200)

    # Content test
    def test_gallery_upload_page_check_content_is_correct(self):
        gallery_upload_page = self.client.get('/gallery/upload_image/')
        self.assertTemplateUsed(gallery_upload_page, "gallery/gallery_form.html")
        gallery_upload_page_template_output = render_to_response("gallery/gallery_form.html").content
        self.assertEqual(gallery_upload_page.content, gallery_upload_page_template_output)

    # Form tests
    def test_gallery_form_success(self):
        form = GalleryForm({
            'image': 'testimage.jpg',
            'description': 'testimage description'
        })
        self.assertTrue(form.is_valid())

    def test_gallery_form_with_missing_image(self):
        form = GalleryForm({
            'description': 'testimage description'
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please select a file",
                                 form.full_clean())
