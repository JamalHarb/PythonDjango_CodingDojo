from datetime import datetime
from distutils.log import error
from django.shortcuts import render, redirect
from . import models
from django.contrib import messages

# Create your views here.
def display_shows(request):
    context = {
        'shows': models.showAllTVshows()
    }
    return render(request, 'display_shows.html', context)

def add_show(request):
    return render(request, 'add_show.html')

def create_show(request):
    errors = models.Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for value in errors.values():
            messages.error(request, value)
        return redirect('/shows/new')
    models.createTVShow(request)
    show = models.showLastTVShow()
    print('+'*100)
    print(request.POST['release-date'])
    print(datetime.now())
    print('+'*100)
    return redirect(f'/shows/{show.id}')

def show_info(request, id):
    context = {
        'show': models.getTVShow(id=id)
    }
    return render(request, 'show_info.html', context)

def edit_show(request, id):
    context = {
        'show': models.getTVShow(id)
    }
    return render(request, 'edit.html', context)

def update_show(request):
    errors = models.Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for value in errors.values():
            messages.error(request, value)
        return redirect('/shows/'+request.POST['showId']+'/edit')
    models.updateTVShow(request)
    return redirect('/shows/'+request.POST['showId'])

def delete_show(request, id):
    show = models.deleteTVShow(id)
    return redirect('/shows')