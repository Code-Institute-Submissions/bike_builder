from django.test import TestCase
from django.shortcuts import render_to_response
from models import User
from views import profile, register, login, edit_profile
from forms import UserRegistrationForm
from django import forms
from django.conf import settings
from django.core.urlresolvers import resolve


class AccountsAppTest(TestCase):

    # Register page
    # URL test
    def test_register_page_resolves(self):
        get_register_page = resolve('/register/')
        self.assertEqual(get_register_page.func, register)

    # Status code test
    def test_register_page_status_code_is_okay(self):
        register_page = self.client.get('/register/')
        self.assertEqual(register_page.status_code, 200)

    # Content test
    def test_register_page_check_content_is_correct(self):
        register_page = self.client.get('/register/')
        self.assertTemplateUsed(register_page, "accounts/register.html")
        register_page_template_output = render_to_response("accounts/register.html").content
        self.assertEqual(register_page.content, register_page_template_output)

    # Registration tests
    def test_registration_form_success(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': 'testpassword1',
            'password2': 'testpassword1',
        })
        self.assertTrue(form.is_valid())

    def test_registration_form_fails_with_missing_email(self):
        form = UserRegistrationForm({
            'password1': 'testpassword1',
            'password2': 'testpassword1',
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your email address",
                                 form.full_clean())

    def test_registration_form_fails_with_missing_password1(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password2': 'testpassword2',
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Passwords do not match",
                                 form.full_clean())

    def test_registration_form_fails_with_missing_password2(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': 'testpassword1',
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Passwords do not match",
                                 form.full_clean())

    def test_registration_form_fails_with_passwords_that_dont_match(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'password1': 'testpassword1',
            'password2': 'testpassword2',
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Passwords do not match",
                                 form.full_clean())

    # Model test
    # user creation success:
    def test_manager_create(self):
        user = User.objects._create_user(None, "test@test.com", "password", False, False)
        self.assertIsNotNone(user)
    # user creation failure:
        with self.assertRaises(ValueError):
            user = User.objects._create_user(None, None, "password", False, False)

    # Login page
    # URL test
    def test_login_page_resolves(self):
        get_login_page = resolve('/login/')
        self.assertEqual(get_login_page.func, login)

    # Status code test
    def test_login_page_status_code_is_okay(self):
        login_page = self.client.get('/login/')
        self.assertEqual(login_page.status_code, 200)

    # Content test
    def test_login_page_check_content_is_correct(self):
        login_page = self.client.get('/login/')
        self.assertTemplateUsed(login_page, "accounts/login.html")
        login_page_template_output = render_to_response("accounts/login.html").content
        self.assertEqual(login_page.content, login_page_template_output)

    # Home page is rendered following successful login
    def setUp(self):
        super(AccountsAppTest, self).setUp()
        self.user = User.objects.create(username='testuser')
        self.user.set_password('testpass1')
        self.user.save()
        self.login = self.client.login(username='testuser',
                                       password='testpass1')
        self.assertEqual(self.login, True)

    def test_home_page_rendered_after_login(self):
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, "home/home.html")
        home_page_template_output = render_to_response("home/home.html", {'user': self.user}).content
        self.assertEqual(home_page.content, home_page_template_output)

    # Profile page
    # URL test
    def test_profile_page_resolves(self):
        get_profile_page = resolve('/profile/')
        self.assertEqual(get_profile_page.func, profile)

    # Status code test
    def test_profile_page_status_code_is_okay(self):
        profile_page = self.client.get('/profile/')
        self.assertEqual(profile_page.status_code, 200)

    # Content test
    def test_profile_page_check_content_is_correct(self):
        profile_page = self.client.get('/profile/')
        self.assertTemplateUsed(profile_page, "accounts/profile.html")
        profile_page_template_output = render_to_response("accounts/profile.html").content
        self.assertEqual(profile_page.content, profile_page_template_output)

    # Edit Profile page
    # URL test
    def test_edit_profile_page_resolves(self):
        get_edit_profile_page = resolve('/edit_profile/')
        self.assertEqual(get_edit_profile_page.func, edit_profile)

    # Status code test
    def test_edit_profile_page_status_code_is_okay(self):
        edit_profile_page = self.client.get('/profile/edit_profile/')
        self.assertEqual(edit_profile_page.status_code, 200)

    # Content test
    def test_edit_profile_page_check_content_is_correct(self):
        edit_profile_page = self.client.get('/profile/edit_profile/')
        self.assertTemplateUsed(edit_profile_page, "accounts/profile_form.html")
        edit_profile_page_template_output = render_to_response("accounts/profile_form.html").content
        self.assertEqual(edit_profile_page.content, edit_profile_page_template_output)
