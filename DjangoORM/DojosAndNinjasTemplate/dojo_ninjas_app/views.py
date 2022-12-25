from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        'dojos': Dojo.objects.all(),
    }
    return render(request, 'index.html', context)

def add_dojo(request):
    Dojo.objects.create(name=request.POST['dojo-name'], city=request.POST['city'], state=request.POST['state'])
    return redirect('/')

def add_ninja(request):
    Ninja.objects.create(first_name=request.POST['first-name'], last_name=request.POST['last-name'], dojo=Dojo.objects.get(id=request.POST['select-dojo']))
    return redirect('/')

def delete_dojo(request):
    dojo = Dojo.objects.get(id=request.POST['which-dojo'])
    dojo.delete()
    return redirect('/')