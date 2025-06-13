from django.test import TestCase, RequestFactory
from records.forms import CustomSignupForm


class CustomSignupFormTests(TestCase):
    """
    Unit tests for CustomSignupForm covering field validation
    and user creation logic via the save() method.
    """

    def setUp(self):
        self.factory = RequestFactory()

    def make_form(self, **overrides):
        """
        Helper to create a valid CustomSignupForm instance
        with optional field overrides for targeted tests.
        """
        data = {
            'email': 'user@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password1': 'testpass123',
            'password2': 'testpass123'
        }
        data.update(overrides)
        return CustomSignupForm(data=data)

    def test_valid_form(self):
        """Form should be valid with all required fields correctly filled."""
        form = self.make_form()
        self.assertTrue(form.is_valid())

    def test_blank_email(self):
        """Form should be invalid if email is blank or whitespace."""
        form = self.make_form(email='   ')
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_blank_first_name(self):
        """Form should be invalid if first name is blank or whitespace."""
        form = self.make_form(first_name='   ')
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)

    def test_invalid_first_name_characters(self):
        """Form should be invalid if first name contains invalid characters."""
        form = self.make_form(first_name='Test123!')
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)

    def test_blank_last_name(self):
        """Form should be invalid if last name is blank or whitespace."""
        form = self.make_form(last_name='   ')
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors)

    def test_save_method_creates_user_with_expected_fields(self):
        """
        CustomSignupForm.save() should assign email, names,
        and a 30-character UUID-based username.
        """
        request = self.factory.post('/accounts/signup/')
        request.session = {}

        form = self.make_form()
        self.assertTrue(form.is_valid())
        user = form.save(request=request)
        self.assertEqual(user.email, 'user@example.com')
        self.assertEqual(user.first_name, 'Test')
        self.assertEqual(user.last_name, 'User')
        self.assertEqual(len(user.username), 30)
