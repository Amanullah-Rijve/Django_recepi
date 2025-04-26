from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Home page")

def about(request):
    return HttpResponse("about page")

def skill(request):
    return HttpResponse("Skill page")

def project(request):
    return HttpResponse("project page")

def contact(request):
    return HttpResponse("contact page")

