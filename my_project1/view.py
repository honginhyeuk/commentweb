# my_project1/view.py

from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request, "django.html")

def hey_man(request):
    return render(request, "daum.html")
