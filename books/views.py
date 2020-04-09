from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .forms import CommentForm
from .models import Book, Comment
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class HomeListView(ListView):
    model = Book
    template_name = 'book/home.html'
    context_object_name = 'books'


class BookListView(ListView):
    queryset = Book.objects.order_by('-id')[:8]
    template_name = 'book/novelty.html'
    context_object_name = 'books'


def book_detail_view(request, pk):
    post = get_object_or_404(Book, pk=pk)
    comments = Comment.objects.filter(post=post).order_by('-id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            username = request.POST.get('username')
            text = request.POST.get('text')
            comment = Comment.objects.create(post=post, username=username, text=text)
            comment.save()
    else:
        comment_form = CommentForm()

    context = {'books': post, 'comments': comments, 'comment_form': comment_form}
    return render(request, 'book/detail.html', context)


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
    context_object_name = 'books'


class BookDelete(DeleteView):
    model = Book
    template_name = 'book/delete.html'
    success_url = reverse_lazy('home')
    context_object_name = 'books'
