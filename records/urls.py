"""
URL configuration for the records app.

Maps record-related views to URLs for listing, creating, updating,
viewing, and deleting vinyl records.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('records/', views.record_list, name='record_list'),
    path('records/add/', views.record_create, name='record_create'),
    path('records/<int:pk>/', views.record_detail, name='record_detail'),
    path('records/<int:pk>/edit/', views.record_update, name='record_update'),
    path('records/<int:pk>/delete/', views.record_delete, name='record_delete'),
]
