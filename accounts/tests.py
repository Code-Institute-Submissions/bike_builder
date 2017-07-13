from django.test import TestCase
from django.shortcuts import render_to_response
from models import User
from views import profile, register, login, edit_profile
from forms import UserRegistrationForm
from django import forms
from django.core.urlresolvers import resolve


class AccountsAppTest(TestCase):

    def setUp(self):
        """
        create a user and log them in
        """
        super(AccountsAppTest, self).setUp()
        self.user = User.objects.create(username='testuser')
        self.user.set_password('testpass1')
        self.user.save()
        self.login = self.client.login(username='testuser',
                                       password='testpass1')
        self.assertEqual(self.login, True)

    def test_register_page_resolves(self):
        register_page = resolve('/accounts/register/')
        self.assertEqual(register_page.func, register)

    def test_register_page_status_code_is_okay(self):
        register_page = self.client.get('/accounts/register/')
        self.assertEqual(register_page.status_code, 200)

    def test_registration_form_success(self):
        form = UserRegistrationForm({
            'email': 'test1@test.com',
            'public_name': 'test name 1',
            'password1': 'testpassword1',
            'password2': 'testpassword1'
        })
        self.assertTrue(form.is_valid())

    def test_registration_form_fails_with_missing_email(self):
        form = UserRegistrationForm({
            'public_name': 'test name 2',
            'password1': 'testpassword1',
            'password2': 'testpassword1'
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your email address",
                                 form.full_clean())

    def test_registration_form_fails_with_missing_public_name(self):
        form = UserRegistrationForm({
            'email': 'test6@test.com',
            'password1': 'testpassword1',
            'password2': 'testpassword1'
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please fill in this field",
                                 form.full_clean())

    def test_registration_form_fails_with_missing_password1(self):
        form = UserRegistrationForm({
            'email': 'test3@test.com',
            'public_name': 'test name 3',
            'password2': 'testpassword1'
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Passwords do not match",
                                 form.full_clean())

    def test_registration_form_fails_with_missing_password2(self):
        form = UserRegistrationForm({
            'email': 'test4@test.com',
            'public_name': 'test name 4',
            'password1': 'testpassword1'
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Passwords do not match",
                                 form.full_clean())

    def test_registration_form_fails_with_passwords_that_dont_match(self):
        form = UserRegistrationForm({
            'email': 'test5@test.com',
            'public_name': 'test name',
            'password1': 'testpassword1',
            'password2': 'testpassword2'
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Passwords do not match",
                                 form.full_clean())

    def test_login_page_resolves(self):
        login_page = resolve('/accounts/login/')
        self.assertEqual(login_page.func, login)

    def test_login_page_status_code_is_okay(self):
        login_page = self.client.get('/accounts/login/')
        self.assertEqual(login_page.status_code, 200)

    def test_profile_page_rendered_after_login(self):
        profile_page = self.client.get('/accounts/profile/')
        self.assertTemplateUsed(profile_page, "accounts/profile.html")
        profile_page_template_output = render_to_response("accounts/profile.html",
                                                          {'user': self.user}).content
        self.assertHTMLEqual(profile_page.content, profile_page_template_output)

    def test_profile_page_resolves(self):
        profile_page = resolve('/accounts/profile/')
        self.assertEqual(profile_page.func, profile)

    def test_profile_page_status_code_is_okay(self):
        profile_page = self.client.get('/accounts/profile/')
        self.assertEqual(profile_page.status_code, 200)

    def test_edit_profile_page_resolves(self):
        edit_profile_page = resolve('/accounts/profile/edit_profile/')
        self.assertEqual(edit_profile_page.func, edit_profile)

    def test_edit_profile_page_status_code_is_okay(self):
        edit_profile_page = self.client.get('/accounts/profile/edit_profile/')
        self.assertEqual(edit_profile_page.status_code, 200)
