from django.shortcuts import render, redirect
from django.contrib import messages
from . import models

# Create your views here.
def index(request):
    return render(request, 'index.html')

def check_register(request):
    reg_errors = models.register_errors(request)
    if reg_errors:
        for value in reg_errors.values():
            messages.error(request, value)
        return redirect('/')
    models.register(request)
    return redirect('/success')

def check_login(request):
    log_errors = models.login_errors(request)
    if log_errors:
        for value in log_errors.values():
            messages.error(request, value)
        return redirect('/')
    models.login(request)
    return redirect('/success')

def success(request):
    return render(request, 'success.html')

def logout(request):
    request.session.clear()
    return redirect('/')