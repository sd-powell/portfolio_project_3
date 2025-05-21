from django import forms
from django.forms import inlineformset_factory
from allauth.account.forms import SignupForm
from .models import Record, Track


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
            'cover_image',
            'rating']

        labels = {
            'title': 'Record Title',
            'artist': 'Artist Name',
            'year': 'Release Year',
            'genre': 'Genre',
            'cover_image': 'Cover Image',
            'rating': 'Rating (1-5)',
        }

        help_texts = {
            'title': 'Enter the title of the record.',
            'artist': 'Enter the name of the artist or band.',
            'year': 'Enter the release year (4 digits - e.g. 1982).',
            'genre': 'Select the genre of the record from the dropdown.',
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
            'cover_image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Upload cover image'
            }),
            'rating': forms.Select(attrs={
                'class': 'form-control',
            }),
        }


class TrackForm(forms.ModelForm):
    """
    Form for users to create and edit
    individual tracks linked to a Record.

    Includes metadata fields such as title, position,
    duration, BPM and musical key with user-friendly
    labels, validation, and form styling.
    """

    class Meta:
        model = Track
        fields = [
            'title',
            'position',
            'duration',
            'bpm',
            'key'
        ]

        labels = {
            'title': 'Track Title',
            'position': 'Track Position',
            'duration': 'Duration',
            'bpm': 'BPM (Beats Per Minute)',
            'key': 'Musical Key (Camelot Notation)',
        }

        help_texts = {
            'title': 'Enter the name of the track.',
            'position': 'Track position on vinyl (e.g. A1, B2).',
            'duration': 'Duration in minutes and seconds (e.g. 4:32).',
            'bpm': 'Typical range is 60–180 (optional).',
            'key': 'Select the track’s key using Camelot notation (optional).',
        }

        error_messages = {
            'title': {
                'required': 'Please enter the title of the track.',
                'max_length': 'Title is too long (255 characters max).',
            },
            'bpm': {
                'invalid': 'Please enter a valid number for BPM.',
                'min_value': 'Minimum BPM is 24.',
                'max_value': 'Maximum BPM is 1000.',
            },
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Around The World'
            }),
            'position': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. A1'
            }),
            'duration': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 4:32'
            }),
            'bpm': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 120'
            }),
            'key': forms.Select(attrs={
                'class': 'form-control'
            }),
        }


# Define the inline formset for Track entries related to Record
TrackFormSet = inlineformset_factory(
    parent_model=Record,
    model=Track,
    form=TrackForm,
    fields=['title', 'position', 'duration', 'bpm', 'key'],
    extra=1,
    can_delete=True
)


class CustomSignupForm(SignupForm):
    """
    Custom signup form that adds first and last name fields
    to the default Allauth form.
    """
    first_name = forms.CharField(
        max_length=30,
        label='First Name',
        required=False
        )
    last_name = forms.CharField(
        max_length=30,
        label='Last Name',
        required=False
        )

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
