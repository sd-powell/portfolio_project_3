from django import forms
from .models import Record


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['title', 'artist', 'year', 'genre', 'bpm', 'key', 'cover_image', 'rating']
