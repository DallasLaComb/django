from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def second(request):
    return render(request, 'second.html')