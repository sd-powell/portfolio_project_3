from django import forms
from django.forms import inlineformset_factory
from django.core.exceptions import ValidationError
from allauth.account.forms import SignupForm
from .models import Record, Track
import re


# --- Validator Functions ---
def validate_no_whitespace_only(value):
    """
    Ensures the input is not only whitespace.
    """
    if not re.match(r"\S(.*\S)?", value):
        raise ValidationError(
            "This field cannot be blank or contain only whitespace."
            )


def validate_duration_format(value):
    """
    Ensure the duration is in M:SS or MM:SS format with seconds < 60.
    """
    match = re.match(r'^(\d{1,2}):([0-5]\d)$', value)
    if not match:
        raise ValidationError(
            "Duration must be in the format M:SS or MM:SS "
            "with seconds between 00 and 59 (e.g. 4:32)."
        )


# --- Form Helper Functions ---
def form_control_input(placeholder):
    """
    Generate a styled TextInput widget with Bootstrap 'form-control' class.

    Args:
        placeholder (str): Placeholder text to display inside the input field.

    Returns:
        TextInput: A Django TextInput widget instance with custom styling.
    """
    return forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': placeholder
    })


def form_control_number(placeholder, min_val=None, max_val=None):
    """
    Generate a styled NumberInput widget with optional min and max values.

    Args:
        placeholder (str): Placeholder text for the input field.
        min_val (int, optional): Minimum value allowed.
        max_val (int, optional): Maximum value allowed.

    Returns:
        NumberInput: Styled Django NumberInput widget.
    """
    attrs = {'class': 'form-control', 'placeholder': placeholder}
    if min_val is not None:
        attrs['min'] = min_val
    if max_val is not None:
        attrs['max'] = max_val
    return forms.NumberInput(attrs=attrs)


def form_control_select():
    """
    Generate a styled Select widget with Bootstrap 'form-control' class.

    Returns:
        Select: Styled Django Select widget.
    """
    return forms.Select(attrs={'class': 'form-control'})


def form_control_file():
    """
    Generate a styled ClearableFileInput widget for file uploads.

    Returns:
        ClearableFileInput: Styled file input widget.
    """
    return forms.ClearableFileInput(attrs={'class': 'form-control'})


# --- Forms ---
class RecordForm(forms.ModelForm):
    """
    Form for users to create and edit
    Record entries with styling and validation.
    """

    title = forms.CharField(
        max_length=255,
        validators=[validate_no_whitespace_only],
        widget=form_control_input('e.g. Discovery'),
        label='Record Title',
        help_text='Enter the title of the record.',
        error_messages={
            'required': 'Please enter the title of the record.',
            'max_length': 'Title is too long (255 characters max).',
        }
    )

    artist = forms.CharField(
        max_length=255,
        validators=[validate_no_whitespace_only],
        widget=form_control_input('e.g. Daft Punk'),
        label='Artist Name',
        help_text='Enter the name of the artist or band.',
        error_messages={
            'required': 'Please enter the artist\'s name.',
            'max_length': 'Artist name is too long (255 characters max).',
        }
    )

    year = forms.IntegerField(
        min_value=1000,
        max_value=9999,
        widget=form_control_number('e.g. 2001', 1000, 9999),
        label='Release Year',
        help_text='Enter the release year (4 digits - e.g. 1982).',
        error_messages={
            'invalid': 'Please enter a valid 4-digit year.',
            'min_value': 'Year must be no earlier than 1000.',
            'max_value': 'Year must be no later than 9999.',
        }
    )

    genre = forms.ChoiceField(
        choices=Record._meta.get_field('genre').choices,
        widget=form_control_select(),
        label='Genre',
        help_text='Select the genre of the record from the dropdown.'
    )

    cover_image = forms.ImageField(
        required=False,
        widget=form_control_file(),
        label='Cover Image',
        help_text='Upload a cover image for the record (optional).'
    )

    rating = forms.ChoiceField(
        choices=Record._meta.get_field('rating').choices,
        widget=form_control_select(),
        label='Rating (1-5)',
        help_text='Rate this record from 1 (worst) to 5 (best).',
        error_messages={
            'invalid_choice': 'Select a valid rating between 1 and 5.',
        }
    )

    class Meta:
        model = Record
        fields = [
            'title',
            'artist',
            'year',
            'genre',
            'cover_image',
            'rating']


class TrackForm(forms.ModelForm):
    """
    Form for users to create and edit
    individual tracks linked to a Record.

    Includes metadata fields such as title, position,
    duration, BPM and musical key with user-friendly
    labels, validation, and form styling.
    """

    title = forms.CharField(
        max_length=255,
        validators=[validate_no_whitespace_only],
        widget=form_control_input('e.g. Around The World'),
        label='Track Title',
        help_text='Enter the name of the track.',
        error_messages={
            'required': 'Please enter the title of the track.',
            'max_length': 'Title is too long (255 characters max).',
        }
    )

    position = forms.CharField(
        max_length=10,
        widget=form_control_input('e.g. A1'),
        label='Track Position',
        help_text='Track position on vinyl (e.g. A1, B2).'
    )

    duration = forms.CharField(
        max_length=10,
        validators=[validate_duration_format],
        widget=form_control_input('e.g. 4:32'),
        label='Duration',
        help_text='Duration in minutes and seconds (e.g. 4:32).',
        error_messages={
            'required': 'Please enter the duration.',
            'max_length': 'Duration is too long (10 characters max).',
        }
    )

    bpm = forms.IntegerField(
        required=False,
        min_value=24,
        max_value=1000,
        widget=form_control_number('e.g. 120'),
        label='BPM (Beats Per Minute)',
        help_text='Typical range is 60–180 (optional).',
        error_messages={
            'invalid': 'Please enter a valid number for BPM.',
            'min_value': 'Minimum BPM is 24.',
            'max_value': 'Maximum BPM is 1000.',
        }
    )

    key = forms.CharField(
        required=False,
        widget=form_control_select(),
        label='Musical Key (Camelot Notation)',
        help_text='Select the track’s key using Camelot notation (optional).'
    )

    class Meta:
        model = Track
        fields = [
            'title',
            'position',
            'duration',
            'bpm',
            'key'
        ]


# --- Inline Formset ---
TrackFormSet = inlineformset_factory(
    parent_model=Record,
    model=Track,
    form=TrackForm,
    fields=['title', 'position', 'duration', 'bpm', 'key'],
    extra=1,
    can_delete=False
)


# --- Custom Signup ---
class CustomSignupForm(SignupForm):
    """
    Custom signup form that adds first and last name fields
    to the default Allauth form.
    """
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Email'}
            )
    )

    first_name = forms.CharField(
        max_length=30,
        label='First Name',
        required=True,
        widget=form_control_input('First Name')
    )
    last_name = forms.CharField(
        max_length=30,
        label='Last Name',
        required=True,
        widget=form_control_input('Last Name')
    )

    def clean_email(self):
        if not (email := self.cleaned_data.get('email', '').strip()):
            raise ValidationError("Email cannot be blank.")
        return email

    def clean_first_name(self):
        if not (first := self.cleaned_data.get('first_name', '').strip()):
            raise forms.ValidationError(
                "First name cannot be blank or whitespace."
                )
        if not re.match("^[A-Za-z '-]+$", first):
            raise forms.ValidationError(
                "First name contains invalid characters."
                )
        return first

    def clean_last_name(self):
        if not (last := self.cleaned_data.get('last_name', '').strip()):
            raise forms.ValidationError(
                "Last name cannot be blank or whitespace."
                )
        return last

    def save(self, request):
        user = super().save(request)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
