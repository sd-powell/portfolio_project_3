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
