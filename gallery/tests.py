from django.test import TestCase
from views import gallery, upload_image
from forms import GalleryForm
from django.core.urlresolvers import resolve
from django import forms
from accounts.models import User


class GalleryPageTest(TestCase):

    def setUp(self):
        """
        Create a user and log them in
        """
        super(GalleryPageTest, self).setUp()
        self.user = User.objects.create(username='testuser10')
        self.user.set_password('testpass10')
        self.user.save()
        self.login = self.client.login(username='testuser10',
                                       password='testpass10')
        self.assertEqual(self.login, True)

    def test_gallery_page_resolves(self):
        gallery_page = resolve('/gallery/')
        self.assertEqual(gallery_page.func, gallery)

    def test_gallery_page_status_code_is_okay(self):
        gallery_page = self.client.get('/gallery/')
        self.assertEqual(gallery_page.status_code, 200)

    def test_gallery_upload_page_resolves(self):
        gallery_form_page = resolve('/gallery/upload_image/')
        self.assertEqual(gallery_form_page.func, upload_image)

    def test_gallery_upload_page_status_code_is_okay(self):
        gallery_upload_page = self.client.get('/gallery/upload_image/', follow=True)
        self.assertEqual(gallery_upload_page.status_code, 200)

    def test_gallery_form_with_missing_image(self):
        form = GalleryForm({
            'description': 'testimage description'
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please select a file",
                                 form.full_clean())
