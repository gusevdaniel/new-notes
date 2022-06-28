from django.urls import path
from .views import (
    NoteDetailView,
    NoteCreateView,
    NoteUpdateView,
    NoteDeleteView,
    UserNoteListView
)
from . import views

urlpatterns = [
    path('', views.home, name='notes-home'),
    path('user/', UserNoteListView.as_view(), name='user-notes'),
    path('note/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('note/new/', NoteCreateView.as_view(), name='note-create'),
    path('note/<int:pk>/update/', NoteUpdateView.as_view(), name='note-update'),
    path('note/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
]