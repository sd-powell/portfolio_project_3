from django.contrib import admin

# Register your models here.
from .models import Record


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'user', 'genre', 'year', 'bpm', 'key', 'rating')
    list_filter = ('genre', 'rating', 'key', 'year')
    search_fields = ('title', 'artist', 'user__username')
