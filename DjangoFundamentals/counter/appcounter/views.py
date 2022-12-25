from http.client import HTTPResponse
import re
from django.shortcuts import render, HttpResponse, redirect
def index(request):
    if 'visit' not in request.session:
        request.session['visit']=1

    else:
        request.session['visit']+=1

    return render(request, 'visit.html')

def destroy(request):
    del request.session['visit']
    return redirect('/')

def plus_two(request):
    request.session['visit'] += 1
    return redirect('/')

def plus_num(request):
    request.session['visit'] = request.session['visit'] + int(request.POST['number']) - 1
    return redirect('/')
