from django.shortcuts import render, redirect
from django.views.generic import DetailView
from portfolio.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail

from django.http import HttpResponse
from .models import Job, Intro

def home(request):
    jobs = Job.objects.all()
    context ={
        'jobs':jobs
    }
    return render(request,"jobs/home.html",context)

def intro(request):
    return render(request,"jobs/inc/intro.html")

def say_hello(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        name = request.POST['name']
        message = request.POST['message']
        recepient = str(sub['email'].value())
        send_mail(name, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'jobs/success.html', {'recepient': recepient})
    return render(request, 'jobs/say-hello.html', {'form':sub})

