from django import forms
from .models import Record


class RecordForm(forms.ModelForm):
    """
    Form for users to create and edit
    Record entries with styling and validation.
    """

    class Meta:
        model = Record
        fields = [
            'title',
            'artist',
            'year',
            'genre',
            'bpm',
            'key',
            'cover_image',
            'rating']

        labels = {
            'title': 'Record Title',
            'artist': 'Artist Name',
            'year': 'Release Year',
            'genre': 'Genre',
            'bpm': 'BPM (Beats Per Minute)',
            'key': 'Musical Key (Camelot Notation)',
            'cover_image': 'Cover Image',
            'rating': 'Rating (1-5)',
        }

        help_texts = {
            'title': 'Enter the title of the record.',
            'artist': 'Enter the name of the artist or band.',
            'year': 'Enter the release year (4 digits - e.g. 1982).',
            'genre': 'Select the genre of the record from the dropdown.',
            'bpm': 'Enter the BPM - Typical range is 60–180 (optional).',
            'key': 'Select the key using Camelot notation (optional).',
            'cover_image': 'Upload a cover image for the record (optional).',
            'rating': 'Rate this record from 1 (worst) to 5 (best).',
        }
