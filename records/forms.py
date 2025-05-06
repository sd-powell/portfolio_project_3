from django import forms
from .models import Record


class RecordForm(forms.ModelForm):
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
