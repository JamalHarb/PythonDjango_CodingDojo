from django.shortcuts import render, redirect
import random
from time import localtime, strftime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'log' not in request.session:
        request.session['log'] = []
    if 'time_stamp' not in request.session:
        request.session['time_stamp'] = []
    return render(request, 'index.html')

def process_gold(request):
    request.session['time_stamp'] = strftime("%B %d, %Y %I:%M:%S %p", localtime())
    if request.POST['which_place'] == 'quest':
        rand = random.randint(-50, 50)
        request.session['gold'] += rand
        if rand > 0:
            request.session['log'].insert(0, f"You completed a quest and earned {rand} gold. ({request.session['time_stamp']})")
        elif rand < 0:
            request.session['log'].insert(0, f"You failed a quest and lost {rand} gold. Ouch. ({request.session['time_stamp']})")
        else:
            request.session['log'].insert(0, f"The quest didn't yield any gold. ({request.session['time_stamp']})")
    else:
        rand = random.randint(1, 20)
        request.session['gold'] += rand
        if request.POST['which_place'] == 'farm':
            request.session['log'].insert(0, f"You enterd a farm and earned {rand} gold. ({request.session['time_stamp']})")  
        elif request.POST['which_place'] == 'cave':
            request.session['log'].insert(0, f"You enterd a cave and earned {rand} gold. ({request.session['time_stamp']})")  
        else:
            request.session['log'].insert(0, f"You enterd a house and earned {rand} gold. ({request.session['time_stamp']})") 
    request.session.save()
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')