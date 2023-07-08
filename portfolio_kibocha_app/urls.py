from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('blogs', views.blogs, name='blogs'),
    path('projects', views.projects, name='projects'),
    path('contact-me', views.contact_me, name='contact-me'),
]
