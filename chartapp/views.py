from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    data = "Current data"

    context = {
        "data": data
    }

    return render(request, 'chartapp/index.html', context)