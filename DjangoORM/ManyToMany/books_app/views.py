from django.shortcuts import render, redirect
from .models import *

def all_books(request):
    context = {
        'books': Book.objects.all(),
    }
    return render(request, 'add_book.html', context)

def add_book(request):
    Book.objects.create(title=request.POST['title'], description=request.POST['desc'])
    return redirect('/')

def show_book(request, _id):
    context = {
        'book': Book.objects.get(id=_id),
        'authors': Author.objects.all()
    }
    return render(request, 'show_book.html', context)

def assign_author(request):
    some_book = Book.objects.get(id=request.POST['which-book'])
    some_author = Author.objects.get(id=request.POST['which-author'])
    some_author.books.add(some_book)
    return redirect(f'/books/{some_book.id}')

def all_authors(request):
    context = {
        'authors': Author.objects.all(),
    }
    return render(request, 'add_author.html', context)

def add_author(request):
    Author.objects.create(name=request.POST['first-name']+' '+request.POST['last-name'], notes=request.POST['notes'])
    return redirect('/authors')

def show_author(request, _id):
    context = {
        'books': Book.objects.all(),
        'author': Author.objects.get(id=_id)
    }
    return render(request, 'show_author.html', context)

def assign_book(request):
    some_book = Book.objects.get(id=request.POST['which-book'])
    some_author = Author.objects.get(id=request.POST['which-author'])
    some_book.authors.add(some_author)
    return redirect(f'/authors/{some_author.id}')