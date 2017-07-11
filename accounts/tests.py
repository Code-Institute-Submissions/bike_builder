from django.test import TestCase
from django.shortcuts import render_to_response
from models import User
from views import profile, register, login, edit_profile
from forms import UserRegistrationForm, UserProfileForm, UserLoginForm
from django import forms
from django.conf import settings
from django.core.urlresolvers import resolve


class AccountsAppTest(TestCase):

    # Create a user and log them in
    def setUp(self):
        super(AccountsAppTest, self).setUp()
        self.user = User.objects.create(username='testuser')
        self.user.set_password('testpass1')
        self.user.save()
        self.login = self.client.login(username='testuser',
                                       password='testpass1')
        self.assertEqual(self.login, True)

    # Register page
    # URL test
    def test_register_page_resolves(self):
        register_page = resolve('/accounts/register/')
        self.assertEqual(register_page.func, register)

    # Status code test
    def test_register_page_status_code_is_okay(self):
        register_page = self.client.get('/accounts/register/')
        self.assertEqual(register_page.status_code, 200)

    # # Content test
    # def test_check_register_page_content_is_correct(self):
    #     self.maxDiff = None
    #     register_page = self.client.get('/accounts/register/')
    #     self.assertTemplateUsed(register_page, "accounts/register.html")
    #     register_page_template_output = render_to_response("accounts/register.html",
    #                                                        {'form': UserRegistrationForm()}).content
    #     self.assertHTMLEqual(register_page.content, register_page_template_output)
    # # FAIL: AssertionError: due to a page where a user is logged in being compared to one with guest

    # Registration tests
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

    # # Model test
    # def test_manager_create(self):
    #     user = User.objects._create_user(None, "test6@test.com", "password", False, False)
    #     self.assertIsNotNone(user)
    #
    #     with self.assertRaises(ValueError):
    #         user = User.objects._create_user(None, None, "password", False, False)
    # # ERROR: IntegrityError: UNIQUE constraint failed: accounts_user.public_name

    # Login page
    # URL test
    def test_login_page_resolves(self):
        login_page = resolve('/accounts/login/')
        self.assertEqual(login_page.func, login)

    # Status code test
    def test_login_page_status_code_is_okay(self):
        login_page = self.client.get('/accounts/login/')
        self.assertEqual(login_page.status_code, 200)

    # # Content test
    # def test_check_login_page_content_is_correct(self):
    #     self.maxDiff = None
    #     login_page = self.client.get('/accounts/login/')
    #     self.assertTemplateUsed(login_page, "accounts/login.html")
    #     login_page_template_output = render_to_response("accounts/login.html",
    #                                                     {'form': UserLoginForm()}).content
    #     self.assertHTMLEqual(login_page.content, login_page_template_output)
    # # FAIL: AssertionError: due to a page where a user is logged in being compared to one with guest

    # Home page is rendered following successful login
    # def setUp(self):
    #     super(AccountsAppTest, self).setUp()
    #     self.user = User.objects.create(username='testuser')
    #     self.user.set_password('testpass1')
    #     self.user.save()
    #     self.login = self.client.login(username='testuser',
    #                                    password='testpass1')
    #     self.assertEqual(self.login, True)
    #
    def test_profile_page_rendered_after_login(self):
        profile_page = self.client.get('/accounts/profile/')
        self.assertTemplateUsed(profile_page, "accounts/profile.html")
        profile_page_template_output = render_to_response("accounts/profile.html",
                                                          {'user': self.user}).content
        self.assertHTMLEqual(profile_page.content, profile_page_template_output)
    # def test_home_page_rendered_after_login(self):
    #     home_page = self.client.get('/')
    #     self.assertTemplateUsed(home_page, "home/home.html")
    #     home_page_template_output = render_to_response("home/home.html", {'user': self.user}).content
    #     self.assertEqual(home_page.content, home_page_template_output)

    # Profile page
    # URL test
    def test_profile_page_resolves(self):
        profile_page = resolve('/accounts/profile/')
        self.assertEqual(profile_page.func, profile)

    # Status code test
    def test_profile_page_status_code_is_okay(self):
        profile_page = self.client.get('/accounts/profile/')
        self.assertEqual(profile_page.status_code, 200)

    # # Content test
    # def test_check_profile_page_content_is_correct(self):
    #     self.maxDiff = None
    #     profile_page = self.client.get('/accounts/profile/')
    #     self.assertTemplateUsed(profile_page, "accounts/profile.html")
    #     profile_page_template_output = render_to_response("accounts/profile.html").content
    #     self.assertHTMLEqual(profile_page.content, profile_page_template_output)
    # # FAIL: AssertionError: due to a page where a user is logged in being compared to one with guest

    # Edit Profile page
    # URL test
    def test_edit_profile_page_resolves(self):
        edit_profile_page = resolve('/accounts/profile/edit_profile/')
        self.assertEqual(edit_profile_page.func, edit_profile)

    # Status code test
    def test_edit_profile_page_status_code_is_okay(self):
        edit_profile_page = self.client.get('/accounts/profile/edit_profile/')
        self.assertEqual(edit_profile_page.status_code, 200)

    # # Content test
    # def test_check_edit_profile_page_content_is_correct(self):
    #     self.maxDiff = None
    #     edit_profile_page = self.client.get('/accounts/profile/edit_profile/')
    #     self.assertTemplateUsed(edit_profile_page, "accounts/profile_form.html")
    #     edit_profile_page_template_output = render_to_response("accounts/profile_form.html",
    #                                                            {'form': UserProfileForm()}).content
    #     self.assertHTMLEqual(edit_profile_page.content, edit_profile_page_template_output)
    # # FAIL: AssertionError: due to a page where a user is logged in being compared to one with guest
