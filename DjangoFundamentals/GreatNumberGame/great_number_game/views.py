from django.shortcuts import render, redirect
import random

def index(request):
    if 'rand' not in request.session:
        request.session['rand'] = random.randint(1, 100)
    return render(request, "index.html")

def handle_guess(request):
    request.session['guess'] = int(request.POST['guess'])
    return redirect('/')

def right_guess(request):
    request.session['rand'] = random.randint(1, 100)
    del request.session['guess']
    return redirect('/')