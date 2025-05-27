from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from records.forms import RecordForm
from records.models import GENRE_CHOICES, RATING_CHOICES


class RecordFormTests(TestCase):
    """
    Unit tests for the RecordForm used to create and edit Record entries.
    """

    def setUp(self):
        self.valid_data = {
            'title': 'Discovery',
            'artist': 'Daft Punk',
            'year': 2001,
            'genre': 'House',
            'rating': 5,
        }

    def test_record_form_valid(self):
        """
        Form should be valid when all required fields are correctly filled.
        """
        form = RecordForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_record_form_missing_required_fields(self):
        """
        Form should be invalid if required fields like title or artist are missing.
        Year is optional based on model settings.
        """
        form = RecordForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        self.assertIn('artist', form.errors)

    def test_record_form_invalid_year(self):
        """
        Form should be invalid if the year is non-numeric.
        """
        data = self.valid_data.copy()
        data['year'] = 'not_a_year'
        form = RecordForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('year', form.errors)

