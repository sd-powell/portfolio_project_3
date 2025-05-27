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
