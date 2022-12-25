from django.shortcuts import render

def show_form(request):
    return render(request, "form.html")

def show_results(request):
    context = {
        "name": request.POST['name'],
        "loc": request.POST['location'],
        "lang": request.POST['language'],
        "comm": request.POST['comment']
    }
    return render(request, "results.html", context)
