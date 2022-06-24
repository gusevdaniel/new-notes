from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Note


def home(request):
    return render(request, 'notes/home.html')


class UserNoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/user_notes.html'
    context_object_name = 'notes'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Note.objects.filter(author=user).order_by('-date_posted')


class NoteDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Note

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.author:
            return True
        return False


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.author:
            return True
        return False


class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    success_url = '/'

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.author:
            return True
        return False