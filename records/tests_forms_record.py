from django.test import TestCase
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile

from records.forms import RecordForm
from records.models import GENRE_CHOICES, RATING_CHOICES


class RecordFormTests(TestCase):
    """
    Unit tests for RecordForm validating required fields, year bounds,
    rating choices, cover image uploads, and whitespace handling.
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
        """Test that RecordForm is valid with all
        required fields correctly filled."""
        form = RecordForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_missing_required_fields(self):
        """Test that RecordForm is invalid if title and artist are missing."""
        form = RecordForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        self.assertIn('artist', form.errors)

    def test_invalid_year(self):
        """Test that RecordForm is invalid if year is not numeric."""
        data = self.valid_data.copy()
        data['year'] = 'not_a_year'
        form = RecordForm(data=data)
        self.assertFalse(form.is_valid())

    def test_invalid_rating_choice(self):
        """Test that RecordForm is invalid with an undefined rating value."""
        data = self.valid_data.copy()
        data['rating'] = 99
        form = RecordForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors)

    def test_year_boundaries(self):
        """Test that RecordForm is valid for
        boundary year values (1000, 9999)."""
        for year in [1000, 9999]:
            data = self.valid_data.copy()
            data['year'] = year
            form = RecordForm(data=data)
            self.assertTrue(form.is_valid())

    def test_year_too_low(self):
        """Test that RecordForm is invalid with year below 1000."""
        data = self.valid_data.copy()
        data['year'] = 999
        form = RecordForm(data=data)
        self.assertFalse(form.is_valid())

    def test_year_too_high(self):
        """Test that RecordForm is invalid with year above 9999."""
        data = self.valid_data.copy()
        data['year'] = 10000
        form = RecordForm(data=data)
        self.assertFalse(form.is_valid())

    def test_title_whitespace_only(self):
        """Test that RecordForm is invalid when title is only whitespace."""
        data = self.valid_data.copy()
        data['title'] = '   '
        form = RecordForm(data=data)
        self.assertFalse(form.is_valid())

    def test_artist_whitespace_only(self):
        """Test that RecordForm is invalid when artist is only whitespace."""
        data = self.valid_data.copy()
        data['artist'] = '   '
        form = RecordForm(data=data)
        self.assertFalse(form.is_valid())

    def test_cover_image_upload(self):
        """Test that RecordForm accepts a minimal valid image file upload."""
        image_data = BytesIO()
        image = Image.new('RGB', (50, 50), color='red')
        image.save(image_data, format='PNG')
        image_data.seek(0)

        image_file = SimpleUploadedFile(
            name='test.png',
            content=image_data.read(),
            content_type='image/png'
        )

        form = RecordForm(data=self.valid_data, files={
            'cover_image': image_file
            })
        self.assertTrue(form.is_valid())
