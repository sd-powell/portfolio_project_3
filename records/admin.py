"""
Admin configuration for the Record and Track models in Vinyl Crate.

Includes list display, filtering, and search functionality
for efficient record management. Tracks can be added or edited
directly within the Record admin panel using inline forms.
"""


from django.contrib import admin
from django.utils.html import format_html
from .models import Record, Track


# Shared field groups
RECORD_LIST_DISPLAY = (
    'title',
    'artist',
    'user',
    'genre',
    'year',
    'rating',
    'is_staff_pick',
    'cover_thumb'
)
RECORD_LIST_FILTER = ('genre', 'rating', 'year', 'is_staff_pick')
RECORD_SEARCH_FIELDS = ('title', 'artist', 'user__username')

TRACK_LIST_DISPLAY = ('title', 'record', 'position', 'duration', 'bpm', 'key')
TRACK_LIST_FILTER = ('key', 'bpm')
TRACK_SEARCH_FIELDS = ('title', 'record__title', 'record__artist')


class TrackInline(admin.TabularInline):
    """
    Inline admin form for managing Track entries within a Record.
    """
    model = Track
    extra = 1
    fields = ('bpm', 'duration', 'key', 'position', 'title')


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = RECORD_LIST_DISPLAY
    list_filter = RECORD_LIST_FILTER
    search_fields = RECORD_SEARCH_FIELDS
    readonly_fields = ('cover_thumb',)
    inlines = [TrackInline]
    exclude = ('slug',)

    def cover_thumb(self, obj):
        """
        Return an HTML image tag for the record's cover image,
        or fallback text if unavailable or invalid.
        """
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
    """
    Admin configuration for standalone Track model management.
    """
    list_display = TRACK_LIST_DISPLAY
    list_filter = TRACK_LIST_FILTER
    search_fields = TRACK_SEARCH_FIELDS
