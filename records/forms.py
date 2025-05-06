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
        
        error_messages = {
            'title': {
                'required': 'Please enter the title of the record.',
                'max_length': 'Title is too long (255 characters max).',
            },
            'artist': {
                'required': 'Please enter the artist\'s name.',
                'max_length': 'Artist name is too long (255 characters max).',
            },
            'year': {
                'invalid': 'Please enter a valid 4-digit year.',
                'min_value': 'Year must be no earlier than 1000.',
                'max_value': 'Year must be no later than 9999.',
            },
            'bpm': {
                'invalid': 'Please enter a valid number for BPM.',
                'min_value': 'Minimum BPM is 24.',
                'max_value': 'Maximum BPM is 1000.',
            },
            'rating': {
                'invalid_choice': 'Select a valid rating between 1 and 5.',
            },
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Discovery'
            }),
            'artist': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Daft Punk'
            }),
            'year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 2001',
                'min': 1000,
                'max': 9999,
            }),
            'genre': forms.Select(attrs={
                'class': 'form-control',
            }),
            'bpm': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 128'
            }),
            'key': forms.Select(attrs={
                'class': 'form-control',
            }),
            'cover_image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Upload cover image'
            }),
            'rating': forms.Select(attrs={
                'class': 'form-control',
            }),
        }
