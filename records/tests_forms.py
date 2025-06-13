from django.test import TestCase
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile

from records.forms import RecordForm, TrackForm
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
            'genre': GENRE_CHOICES[1][0],
            'rating': RATING_CHOICES[1][0],
        }

    def test_record_form_valid(self):
        """
        Form should be valid when all required fields are correctly filled.
        """
        form = RecordForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_record_form_missing_required_fields(self):
        """
        Form should be invalid if required fields
        like title or artist are missing.
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

    def test_record_form_invalid_rating_choice(self):
        """
        Form should be invalid if rating is not in defined choices.
        """
        data = self.valid_data.copy()
        data['rating'] = 10  # Not in RATING_CHOICES
        form = RecordForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors)

    def test_record_form_year_boundaries(self):
        """
        Form should be valid for boundary years if they match allowed range.
        """
        for year in [1000, 9999]:
            data = self.valid_data.copy()
            data['year'] = year
            form = RecordForm(data=data)
            msg = f"Form should be valid with year {year}"
            self.assertTrue(form.is_valid(), msg)

    def test_record_form_with_cover_image(self):
        """
        Form should accept a minimal valid image file upload.
        """
        image_data = BytesIO()
        image = Image.new('RGB', (100, 100), color='red')
        image.save(image_data, format='PNG')
        image_data.seek(0)

        image_file = SimpleUploadedFile(
            name='test.png',
            content=image_data.read(),
            content_type='image/png'
        )

        data = self.valid_data.copy()
        form = RecordForm(data=data, files={'cover_image': image_file})
        self.assertTrue(form.is_valid(), form.errors)

    def test_title_whitespace_only_invalid(self):
        """
        Form should reject title with only whitespace (custom validator).
        """
        data = self.valid_data.copy()
        data['title'] = '   '
        form = RecordForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        
    def test_artist_whitespace_only_invalid(self):
        """
        Form should reject artist with only whitespace (custom validator).
        """
        data = self.valid_data.copy()
        data['artist'] = '   '
        form = RecordForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('artist', form.errors)

    def test_year_below_minimum(self):
        """Form should be invalid for year below 1000."""
        data = self.valid_data.copy()
        data['year'] = 999
        form = RecordForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('year', form.errors)

    def test_year_above_maximum(self):
        """Form should be invalid for year above 9999."""
        data = self.valid_data.copy()
        data['year'] = 10000
        form = RecordForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('year', form.errors)

    def test_record_form_whitespace_title(self):
        data = self.valid_data.copy()
        data['title'] = '   '
        form = RecordForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_track_form_whitespace_title(self):
        data = self.valid_data.copy()
        data['title'] = '   '
        form = TrackForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
