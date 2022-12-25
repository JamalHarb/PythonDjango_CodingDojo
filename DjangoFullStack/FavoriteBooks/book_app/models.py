from distutils.command.upload import upload
from urllib import request
from django.db import models
from login_registration_app.models import User

# Create your models here.
class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if len(postData['title']) < 1:
            errors['title'] = 'Title is required.'
        if len(postData['desc']) < 5:
            errors['desc'] = 'Description should be at least 2 characters.'
        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(User, related_name='uploaded_books', on_delete=models.CASCADE)
    liked_by = models.ManyToManyField(User, related_name='liked_books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

def get_logged_user(request):
    return User.objects.get(email=request.session['email'])

def book_errors(request):
    return Book.objects.book_validator(request.POST)

def create_book(request):
    user = get_logged_user(request)
    book = Book.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc'],
        uploaded_by = user
    )
    book.liked_by.add(user)

def all_books():
    return Book.objects.all()

def add_favorite(request, id):
    book = Book.objects.get(id=id)
    user = get_logged_user(request)
    book.liked_by.add(user)
    return book

def show_book(id):
    return Book.objects.get(id=id)

def modify_book(request, id):
    book = Book.objects.get(id=id)
    if request.POST['which-btn'] == 'Update':
        book.title = request.POST['title']
        book.desc = request.POST['desc']
        book.save()
    else:
        book.delete()

def unfavorite(request, id):
    book = Book.objects.get(id=id)
    user = get_logged_user(request)
    book.liked_by.remove(user)
    return book