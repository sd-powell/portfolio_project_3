# records/tests_forms_track.py

from django.test import TestCase
from records.forms import TrackForm
from records.models import CAMELOT_KEYS


class TrackFormTests(TestCase):
    """
    Unit tests for TrackForm validating required fields,
    custom validators, and acceptable value ranges.
    """

    def setUp(self):
        self.valid_data = {
            'title': 'Around The World',
            'position': 'A1',
            'duration': '7:10',
            'bpm': 120,
            'key': CAMELOT_KEYS[1][0],
        }

    def assert_invalid_field(self, field, value):
        """
        Helper to assert that setting a specific field to a given value
        causes a validation error in the TrackForm.
        """
        data = self.valid_data.copy()
        data[field] = value
        form = TrackForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn(field, form.errors)

    def test_track_form_valid_data(self):
        """Test that the form is valid with correct input data."""
        form = TrackForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_track_form_missing_title(self):
        """Test that the form is invalid if the title is missing."""
        self.assert_invalid_field('title', '')

    def test_track_form_whitespace_title(self):
        """Test that TrackForm is invalid when title is only whitespace."""
        self.assert_invalid_field('title', '   ')

    def test_track_form_invalid_duration_format_seconds(self):
        """Test that TrackForm is invalid with invalid seconds in duration."""
        self.assert_invalid_field('duration', '4:78')

    def test_track_form_invalid_duration_non_time(self):
        """Test that TrackForm is invalid with non-numeric duration string."""
        self.assert_invalid_field('duration', 'abc')

    def test_track_form_duration_missing(self):
        """Test that TrackForm is invalid with empty duration field."""
        self.assert_invalid_field('duration', '')

    def test_track_form_invalid_bpm_type(self):
        """Test that non-numeric BPM causes a validation error."""
        self.assert_invalid_field('bpm', 'fast')

    def test_track_form_bpm_too_low(self):
        """Test that a BPM below the allowed range is rejected."""
        self.assert_invalid_field('bpm', 10)

    def test_track_form_bpm_too_high(self):
        """Test that a BPM above the allowed range is rejected."""
        self.assert_invalid_field('bpm', 2000)
