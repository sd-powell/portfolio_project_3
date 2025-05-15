"""
Admin configuration for the Record abd Track models in Vinyl Crate.

Provides list display, filtering, and search functionality
for easier record management.
"""


from django.contrib import admin
from django.utils.html import format_html
from .models import Record, Track


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'artist',
        'user',
        'genre',
        'year',
        'rating',
        'cover_thumb',
        )
    list_filter = (
        'genre',
        'rating',
        'year'
        )
    search_fields = (
        'title',
        'artist',
        'user__username'
        )

    readonly_fields = ('cover_thumb',)

    def cover_thumb(self, obj):
        try:
            if obj.cover_image:
                return format_html(
                    '<img src="{}" width="260" style="border-radius:4px;" />',
                    obj.cover_image.url
                    )
        except Exception:
            return "Invalid image"
        return "No image"
    cover_thumb.short_description = 'Cover'


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'record',
        'position',
        'duration',
        'bpm',
        'key',
    )
    list_filter = (
        'key',
        'bpm',
    )
    search_fields = (
        'title',
        'record__title',
        'record__artist',
    )
