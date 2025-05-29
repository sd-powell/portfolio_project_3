from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase, Client
from records.models import Record, GENRE_CHOICES


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
            genre=GENRE_CHOICES[1][0],
            year=2000,
            rating=5,
            user=self.user
        )

    def test_index_view(self):
        """
        Test that the index view loads successfully and uses
        the correct template.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'records/index.html')

    def test_record_list_with_and_without_records(self):
        """
        Test that record_list view loads user records and includes
        staff_picks if no records exist.
        """
        response = self.client.get(reverse('record_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('records', response.context)

        # Remove user records to trigger staff picks
        self.record.delete()
        response = self.client.get(reverse('record_list'))
        self.assertIn('staff_picks', response.context)

    def test_record_detail_view(self):
        """
        Test that the record_detail view loads correctly
        for an existing record.
        """
        url = reverse('record_detail', args=[self.record.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'records/record_detail.html')

    def test_record_create_view_get_and_post(self):
        """
        Test GET and POST requests for record_create view.
        Valid POST should redirect on success.
        """
        response = self.client.get(reverse('record_create'))
        self.assertEqual(response.status_code, 200)

        post_data = {
            'title': 'New Album',
            'artist': 'New Artist',
            'genre': GENRE_CHOICES[1][0],
            'year': 2022,
            'rating': 4,
            'tracks-TOTAL_FORMS': 1,
            'tracks-INITIAL_FORMS': 0,
            'tracks-MIN_NUM_FORMS': 0,
            'tracks-MAX_NUM_FORMS': 1000,
            'tracks-0-title': 'Intro',
        }
        response = self.client.post(reverse('record_create'), post_data)
        self.assertEqual(response.status_code, 302)

    def test_record_delete_get_and_post(self):
        """
        Test that record_delete view shows confirmation on GET
        and deletes record on POST.
        """
        url = reverse('record_delete', args=[self.record.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        url = reverse('record_delete', args=[self.record.pk])
        response = self.client.post(url)
        self.assertRedirects(response, reverse('record_list'))

    def test_record_collection_filters(self):
        """
        Test record_collection view with various GET filters.
        Should load records matching search criteria.
        """
        response = self.client.get(reverse('record_collection'), {
            'search': 'Test',
            'genre': GENRE_CHOICES[2][0],
            'artist': 'Test Artist',
            'rating': 5,
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('records', response.context)

    def test_custom_404_handler(self):
        """
        Test that a non-existent URL triggers the custom 404 handler.
        """
        response = self.client.get('/nonexistent-url/')
        self.assertEqual(response.status_code, 404)


class RecordUpdateViewTests(TestCase):
    """
    Tests for the record_update view, ensuring users can update
    their own records and that permissions, form validation,
    and redirects function correctly.
    """

    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='pass')
        self.other_user = User.objects.create_user(username='user2', password='pass')
        self.record = Record.objects.create(
            title="Original Title",
            artist="Original Artist",
            year=1999,
            genre=GENRE_CHOICES[3][0],
            rating=3,
            user=self.user,
        )
        self.url = reverse('record_update', args=[self.record.pk])

    def test_record_update_get(self):
        """
        Test that the update view loads correctly for the record owner (GET).
        """
        self.client.login(username='user1', password='pass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'records/record_form.html')
        self.assertContains(response, "Original Title")

    def test_record_update_post_valid(self):
        """
        Test that a valid POST request updates the record.
        """
        self.client.login(username='user1', password='pass')
        response = self.client.post(self.url, {
            'title': 'Updated Title',
            'artist': 'Updated Artist',
            'year': 2001,
            'genre': GENRE_CHOICES[3][0],
            'rating': 5,
            'tracks-TOTAL_FORMS': 0,
            'tracks-INITIAL_FORMS': 0,
        })
        self.assertRedirects(response, reverse('record_list'))
        self.record.refresh_from_db()
        self.assertEqual(self.record.title, 'Updated Title')
        self.assertEqual(self.record.rating, 5)

    def test_record_update_post_invalid(self):
        """
        Test that an invalid POST (missing title) returns errors.
        """
        self.client.login(username='user1', password='pass')
        response = self.client.post(self.url, {
            'title': '',
            'artist': 'Updated Artist',
            'year': 2001,
            'genre': GENRE_CHOICES[4][0],
            'rating': 5,
            'tracks-TOTAL_FORMS': 0,
            'tracks-INITIAL_FORMS': 0,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter the title of the record.')

    def test_record_update_permission_denied(self):
        """
        Test that another user cannot update someone else's record.
        """
        self.client.login(username='user2', password='pass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 404)
