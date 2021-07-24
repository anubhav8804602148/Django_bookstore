from django.http import HttpResponse
from django.shortcuts import render

user = "Anubhav Sharma"

def home(request):
    user="Anubhav Sharma"
    page = render(request, "home.html", context={"user":user})
    #print(page)
    return page

def change_display_name(request):
  try:
    print(request.data)
  except:
    pass
  return render(request, "change_name.html", context={})