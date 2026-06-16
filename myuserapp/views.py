from django.shortcuts import render
from django.http import HttpResponse

def Homepage(request):
    return render(request, "home.html")

def Aboutpage(request):
    return render(request, "about.html")
    
def Contactpage(request):
    return render(request, "contact.html")