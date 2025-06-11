"""
URL configuration for the records app.

Defines URL patterns for user interactions with vinyl records, including:
- Homepage with staff picks
- Viewing and managing the user's record list
- Filtering the collection view
- Adding, editing, and deleting records
- Viewing detailed information for a specific record
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('my-records/', views.record_list, name='record_list'),
    path(
        'my-records/collection/',
        views.record_collection,
        name='record_collection'
    ),
    path('add/', views.record_create, name='record_create'),
    path('<int:pk>/edit/', views.record_update, name='record_update'),
    path('<int:pk>/delete/', views.record_delete, name='record_delete'),
    path('<slug:slug>/', views.record_detail, name='record_detail'),
]
