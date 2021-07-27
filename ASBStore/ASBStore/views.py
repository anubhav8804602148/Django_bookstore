from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return render(request, "home.html", {"user":"Anubhav"})

def books(request):
  return HttpResponse("")

def users(request):
  return HttpResponse("")

def login(request):
  return HttpResponse("")

def register(request):
  return HttpResponse("")
