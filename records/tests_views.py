from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from records.models import Record


class RecordViewsTests(TestCase):
    """
    Integration tests for views in the records app,
    covering GET and POST scenarios and common conditions.
    """

    def setUp(self):
        """
        Set up test user and a sample record for use in view tests.
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        self.client.login(username='testuser', password='testpass')
        self.record = Record.objects.create(
            title='Test Album',
            artist='Test Artist',
            genre='Disco',
            year=2000,
            rating=5,
            user=self.user
        )

    def test_index_view(self):
        """
        Test that the index view loads successfully and uses the correct template.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'records/index.html')
        
    def test_record_list_with_and_without_records(self):
        """
        Test that record_list view loads user records and includes staff_picks if no records exist.
        """
        response = self.client.get(reverse('record_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('records', response.context)

        # Remove user records to trigger staff picks
        self.record.delete()
        response = self.client.get(reverse('record_list'))
        self.assertIn('staff_picks', response.context)