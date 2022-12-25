from django.shortcuts import render
from time import localtime, strftime

def show_time(request):
    context = {
        "date": strftime("%A, %d %B, %Y", localtime()),
        "hour": strftime("%I:%M %p", localtime())
    }
    return render(request, 'index.html', context)
