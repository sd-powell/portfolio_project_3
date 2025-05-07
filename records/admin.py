"""
Admin configuration for the Record model in Vinyl Crate.

Provides list display, filtering, and search functionality
for easier record management.
"""


from django.contrib import admin
from .models import Record


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'artist',
        'user',
        'genre',
        'year',
        'bpm',
        'key',
        'rating')
    list_filter = (
        'genre',
        'rating',
        'key',
        'year')
    search_fields = (
        'title',
        'artist',
        'user__username')
