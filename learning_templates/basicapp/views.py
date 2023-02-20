from django.shortcuts import render

# Create your views here.

def index(r):
    return render(r, 'basicapp/index.html', context={'text': 'Hello World', 'number': 100}) 

def other(r):
    return render(r, 'basicapp/other.html') 

def relative(r):
    return render(r, 'basicapp/relative.html') 