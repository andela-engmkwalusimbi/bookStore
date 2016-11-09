from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import BookStore
from .forms import BookForm

# Create your views here.


def list_books(request):
    books = BookStore.objects.all()
    param = request.POST.get('category')
    name = request.POST.get('search_name')
    if param is not None and name is not None:
        books = seachItem(param, name)

    context = {
        'title': 'List of Books',
        'books': books,
        'noResults': "No books found"
    }
    return render(request, 'list.html', context)

def add_books(request):
    book_form = BookForm(request.POST or None)

    if book_form.is_valid():
        instance = book_form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'title': 'Add a new book',
        'form': book_form
    }
    return render(request, 'add_book.html', context)

def seachItem(param, name):
    # method to search depending on what a user entered
    if param == 'category':
        result = BookStore.objects.filter(category__iexact=str(name))
    else:
        result = BookStore.objects.filter(title__icontains=str(name))
    return result
