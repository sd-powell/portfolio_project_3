"""
Admin configuration for the Record model in Vinyl Crate.

Provides list display, filtering, and search functionality
for easier record management.
"""


from django.contrib import admin
from django.utils.html import format_html
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
        'rating',
        'cover_thumb',
        )
    list_filter = (
        'genre',
        'rating',
        'key',
        'year'
        )
    search_fields = (
        'title',
        'artist',
        'user__username'
        )

    readonly_fields = ('cover_thumb',)

    def cover_thumb(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" width="260" style="border-radius:4px;" />', obj.cover_image.url)
        return "No image"
    cover_thumb.short_description = 'Cover'
