from django.shortcuts import render

def index(request):
    return render (request,'core/index.html')

def contact(request):
    return render(request,'core/contact.html')

def about(request):
    return render(request,'core/about.html')

def work(request):
    return render(request,'core/work.html')

def achievements(request):
    return render(request,'core/achievements.html')

