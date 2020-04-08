from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Book
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class HomeListView(ListView):
    model = Book
    template_name = 'book/home.html'
    context_object_name = 'books'


class BookListView(ListView):
    queryset = Book.objects.order_by('-id')[:8]
    template_name = 'book/new.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book/read.html'


class BookRandomView(ListView):
    queryset = Book.objects.order_by('?')[:4]
    template_name = 'book/random.html'
    context_object_name = 'books'
    

class BookCreate(CreateView):
    model = Book
    fields = ['title', 'book', 'author']
    template_name = 'book/create.html'
    success_url = reverse_lazy('home')


class BookUpdate(UpdateView):
    model = Book
    template_name = 'book/update.html'
    fields = ['title', 'book']
    success_url = reverse_lazy('home')


class BookDelete(DeleteView):
    model = Book
    template_name = 'book/delete.html'
    success_url = reverse_lazy('home')
