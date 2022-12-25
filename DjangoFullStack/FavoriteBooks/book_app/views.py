from django.shortcuts import render, redirect
from . import models
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'books': models.all_books(),
        'user': models.get_logged_user(request)
    }
    if 'email' not in request.session:
        return redirect('/')
    return render(request, 'index.html', context)

def add_book(request):
    book_errors = models.book_errors(request)
    if book_errors:
        for value in book_errors.values():
            messages.error(request, value)
        return redirect('/books')
    models.create_book(request)
    return redirect('/books')

def add_favorite_main(request, id):
    models.add_favorite(request, id)
    return redirect('/books')

def add_favorite(request, id):
    book = models.add_favorite(request, id)
    return redirect(f'/books/{book.id}')

def show_book(request, id):
    context = {
        'book': models.show_book(id),
        'logged_user': models.get_logged_user(request)
    }
    return render(request, 'show_book.html', context)

def modify_book(request, id):
    book_errors = models.book_errors(request)
    if book_errors:
        for value in book_errors.values():
            messages.error(request, value)
        return redirect(f'/{id}')
    models.modify_book(request, id)
    return redirect('/books')

def unfavorite(request, id):
    book = models.unfavorite(request, id)
    return redirect(f'/books/{book.id}')