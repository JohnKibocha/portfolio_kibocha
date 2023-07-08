from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def profile(request):
    return render(request, 'profile.html')


def blogs(request):
    return render(request, 'blogs.html')


def contact_me(request):
    return render(request, 'contact-me.html')


def projects(request):
    return render(request, 'projects.html')
