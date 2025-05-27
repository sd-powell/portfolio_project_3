from django.test import TestCase
from records.forms import TrackForm

from records.models import CAMELOT_KEYS


class TrackFormTests(TestCase):
    """
    Unit tests for the TrackForm used to create and edit Track entries.
    Covers validation rules, required fields, and expected widget behaviour.
    """

    def setUp(self):
        self.valid_data = {
            'title': 'Around The World',
            'position': 'A1',
            'duration': '7:10',
            'bpm': 120,
            'key': CAMELOT_KEYS[1][0],
        }

    def test_track_form_valid_data(self):
        """
        Test that the form is valid with correct input data.
        """
        form = TrackForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_track_form_missing_title(self):
        """
        Test that the form is invalid if the title is missing.
        """
        data = self.valid_data.copy()
        data['title'] = ''
        form = TrackForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        
    def test_track_form_invalid_bpm_type(self):
        """
        Test that the form is invalid if BPM is not a number.
        """
        data = self.valid_data.copy()
        data['bpm'] = 'fast'
        form = TrackForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('bpm', form.errors)
        
    def test_track_form_bpm_too_low(self):
        """
        Test that the form is invalid if BPM is below the minimum (24).
        """
        data = self.valid_data.copy()
        data['bpm'] = 10
        form = TrackForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('bpm', form.errors)
        
    def test_track_form_bpm_too_high(self):
        """
        Test that the form is invalid if BPM is above the maximum (1000).
        """
        data = self.valid_data.copy()
        data['bpm'] = 2000
        form = TrackForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('bpm', form.errors)