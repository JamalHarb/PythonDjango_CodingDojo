from django.shortcuts import render, redirect
from . import models

# Create your views here.
def wall(request):
    context = {
        'messages': models.all_messages(),
        'before_30mins': models.time_before_30mins
    }
    if 'email' not in request.session:
        return redirect('/')
    return render(request, 'wall.html', context)

def post_message(request):
    models.create_message(request)
    return redirect('/wall')

def post_comment(request):
    models.create_comment(request)
    return redirect('/wall')

def delete_message(request):
    models.delete_message(request)
    return redirect('/wall')