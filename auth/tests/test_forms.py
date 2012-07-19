from django.utils.unittest import TestCase
from django.forms import EmailField
from django.forms.widgets import PasswordInput

from auth import forms


class TeamFormTest(TestCase):
    def test_forms_should_have_TeamForm(self):
        self.assertTrue(hasattr(forms, 'TeamForm'))

    def test_team_should_have_name_field(self):
        self.assertIn('name', forms.TeamForm.base_fields)


class LoginFormTest(TestCase):
	def test_login_should_have_username_and_password_fields(self):
		self.assertIn('username', forms.LoginForm.base_fields)
		self.assertIn('password', forms.LoginForm.base_fields)

	def test_widget_for_password_field_should_be_password(self):
		field = forms.LoginForm.base_fields['password']
		self.assertIsInstance(field.widget, PasswordInput)

	def test_username_should_have_at_most_60_characters(self):
		field = forms.LoginForm.base_fields['username']
		self.assertEqual(60, field.max_length)

	def test_password_should_have_at_least_6_characters(self):
		field = forms.LoginForm.base_fields['password']
		self.assertEqual(6, field.min_length)

	def test_username_field_should_accept_only_email_values(self):
		field = forms.LoginForm.base_fields['username']
		self.assertIsInstance(field, EmailField)

class SignupFormTest(TestCase):
    def test_signup_form_should_have_email_password_and_same_password_again_fields(self):
        self.assertIn('email', forms.SignupForm.base_fields)
        self.assertIn('password', forms.SignupForm.base_fields)
        self.assertIn('same_password_again', forms.SignupForm.base_fields)
