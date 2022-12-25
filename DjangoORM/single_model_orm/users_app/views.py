from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'index.html', context)

def add_user(request):
    User.objects.create(first_name=request.POST['first-name'], last_name=request.POST['last-name'], email_address=request.POST['email'], age=int(request.POST['age']))
    return redirect('/')