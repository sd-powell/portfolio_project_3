from django.test import TestCase, Client
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from records.forms import CustomSignupForm


class CustomSignupFormTests(TestCase):
    """
    Unit tests for the CustomSignupForm, which adds first and last name
    fields to the default Allauth signup form and saves them to the user model.
    """

    def setUp(self):
        self.valid_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'Str0ng!Pass123',
            'password2': 'Str0ng!Pass123',
            'first_name': 'Test',
            'last_name': 'User',
        }

    def test_form_saves_names_correctly(self):
        """
        Test that first_name and last_name are saved correctly to the user.
        """
        client = Client()
        client.get("/")
        request = client.request().wsgi_request

        form = CustomSignupForm(data=self.valid_data)
        self.assertTrue(form.is_valid(), form.errors)
        
        user = form.save(request)

        self.assertEqual(user.first_name, 'Test')
        self.assertEqual(user.last_name, 'User')
